from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView,
                                  UpdateView, DeleteView, TemplateView)
from django.http import JsonResponse

from .models import Transaction, Status, Type, Category, SubCategory
from .forms import TransactionForm


# ========== ГЛАВНАЯ СТРАНИЦА ==========
class TransactionListView(ListView):
    """Отображает список всех транзакций с фильтрацией."""
    model = Transaction
    template_name = 'main_page/index.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        """Фильтруем транзакции по параметрам GET-запроса."""
        queryset = Transaction.objects.all()

        status = self.request.GET.get('status')
        type_ = self.request.GET.get('type')
        category = self.request.GET.get('category')
        subcategory = self.request.GET.get('subcategory')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')

        if status:
            queryset = queryset.filter(status_id=status)
        if type_:
            queryset = queryset.filter(type_id=type_)
        if category:
            queryset = queryset.filter(category_id=category)
        if subcategory:
            queryset = queryset.filter(subcategory_id=subcategory)
        if start_date:
            queryset = queryset.filter(date__gte=start_date)
        if end_date:
            queryset = queryset.filter(date__lte=end_date)

        return queryset

    def get_context_data(self, **kwargs):
        """Добавляем справочники в контекст для фильтрации."""
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['types'] = Type.objects.all()
        context['categories'] = Category.objects.all()
        context['subcategories'] = SubCategory.objects.all()
        return context


# ========== СОЗДАНИЕ И РЕДАКТИРОВАНИЕ ТРАНЗАКЦИЙ ==========
class TransactionCreateView(CreateView):
    """Создание новой транзакции."""
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        """Передача параметров type_id и category_id в форму."""
        kwargs = super().get_form_kwargs()
        kwargs['type_id'] = self.request.GET.get('type')
        kwargs['category_id'] = self.request.GET.get('category')
        return kwargs


class TransactionUpdateView(UpdateView):
    """Редактирование существующей транзакции."""
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        """Передача выбранных значений типа и категории в форму."""
        kwargs = super().get_form_kwargs()
        type_id = self.object.type.id if self.object.type else None
        category_id = self.object.category.id if self.object.category else None
        kwargs['type_id'] = type_id
        kwargs['category_id'] = category_id
        return kwargs


class TransactionDeleteView(DeleteView):
    """Удаление транзакции с подтверждением."""
    model = Transaction
    template_name = 'dictionaries/confirm_delete.html'
    success_url = reverse_lazy('index')


# ========== СТРАНИЦА УПРАВЛЕНИЯ СПРАВОЧНИКАМИ ==========
class DictionaryListView(TemplateView):
    """Отображает страницу управления справочниками."""
    template_name = 'dictionaries/dictionaries.html'

    def get_context_data(self, **kwargs):
        """Добавляем справочники в контекст."""
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['types'] = Type.objects.all()
        context['categories'] = Category.objects.select_related('type').all()
        context['subcategories'] = SubCategory.objects.select_related('category').all()
        return context


# ========== CRUD ДЛЯ СТАТУСОВ ==========
class StatusCreateView(CreateView):
    model = Status
    fields = ['name']
    template_name = 'dictionaries/form_template.html'
    success_url = reverse_lazy('manage_dictionaries')


class StatusUpdateView(UpdateView):
    model = Status
    fields = ['name']
    template_name = 'dictionaries/form_template.html'
    success_url = reverse_lazy('manage_dictionaries')


class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'dictionaries/confirm_delete.html'
    success_url = reverse_lazy('manage_dictionaries')


# ========== CRUD ДЛЯ ТИПОВ ==========
class TypeCreateView(CreateView):
    model = Type
    fields = ['name']
    template_name = 'dictionaries/form_template.html'
    success_url = reverse_lazy('manage_dictionaries')


class TypeUpdateView(UpdateView):
    model = Type
    fields = ['name']
    template_name = 'dictionaries/form_template.html'
    success_url = reverse_lazy('manage_dictionaries')


class TypeDeleteView(DeleteView):
    model = Type
    template_name = 'dictionaries/confirm_delete.html'
    success_url = reverse_lazy('manage_dictionaries')


# ========== CRUD ДЛЯ КАТЕГОРИЙ ==========
class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'type']
    template_name = 'dictionaries/form_template.html'
    success_url = reverse_lazy('manage_dictionaries')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'type']
    template_name = 'dictionaries/form_template.html'
    success_url = reverse_lazy('manage_dictionaries')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'dictionaries/confirm_delete.html'
    success_url = reverse_lazy('manage_dictionaries')


# ========== CRUD ДЛЯ ПОДКАТЕГОРИЙ ==========
class SubCategoryCreateView(CreateView):
    model = SubCategory
    fields = ['name', 'category']
    template_name = 'dictionaries/form_template.html'
    success_url = reverse_lazy('manage_dictionaries')


class SubCategoryUpdateView(UpdateView):
    model = SubCategory
    fields = ['name', 'category']
    template_name = 'dictionaries/form_template.html'
    success_url = reverse_lazy('manage_dictionaries')


class SubCategoryDeleteView(DeleteView):
    model = SubCategory
    template_name = 'dictionaries/confirm_delete.html'
    success_url = reverse_lazy('manage_dictionaries')


# ========== API ДЛЯ ДИНАМИЧЕСКОГО ВЫБОРА КАТЕГОРИЙ И ПОДКАТЕГОРИЙ ==========
def get_categories(request):
    """API для получения категорий, привязанных к выбранному типу."""
    type_id = request.GET.get("type_id")
    categories = Category.objects.filter(type_id=type_id).values("id", "name")
    return JsonResponse({"categories": list(categories)})


def get_subcategories(request):
    """API для получения подкатегорий, привязанных к выбранной категории."""
    category_id = request.GET.get("category_id")
    subcategories = SubCategory.objects.filter(category_id=category_id).values("id", "name")
    return JsonResponse({"subcategories": list(subcategories)})
