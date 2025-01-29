from django import forms
from django.utils.timezone import now
from .models import Transaction, Category, SubCategory


class TransactionForm(forms.ModelForm):
    """Создание и редактирование транзакций."""

    class Meta:
        model = Transaction
        fields = ['date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'subcategory': forms.Select(attrs={'class': 'form-select'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        type_id = kwargs.pop('type_id', None)
        category_id = kwargs.pop('category_id', None)
        super().__init__(*args, **kwargs)

        # Фильтрация категорий: если указан тип, показываем связанные категории
        self.fields['category'].queryset = Category.objects.filter(
            type_id=type_id) if type_id else Category.objects.all()

        # Фильтрация подкатегорий:
        self.fields['subcategory'].queryset = SubCategory.objects.filter(
            category_id=category_id) if category_id else SubCategory.objects.all()

        # Сохранение выбранных значений (чтобы они не сбрасывались)
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields[
                    'subcategory'].queryset = SubCategory.objects.filter(
                        category_id=category_id)
            except (ValueError, TypeError):
                pass
