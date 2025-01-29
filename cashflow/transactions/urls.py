from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.TransactionListView.as_view(), name='index'),
    path('create/',
         views.TransactionCreateView.as_view(), name='create_transaction'),
    path('edit/<int:pk>/',
         views.TransactionUpdateView.as_view(), name='edit_transaction'),
    path('delete/<int:pk>/',
         views.TransactionDeleteView.as_view(), name='delete_transaction'),
    path("get_categories/",
         views.get_categories, name="get_categories"),
    path("get_subcategories/",
         views.get_subcategories, name="get_subcategories"),

    path('dictionaries/',
         views.DictionaryListView.as_view(), name='manage_dictionaries'),

    # CRUD для статусов
    path('dictionaries/status/add/',
         views.StatusCreateView.as_view(), name='add_status'),
    path('dictionaries/status/<int:pk>/edit/',
         views.StatusUpdateView.as_view(), name='edit_status'),
    path('dictionaries/status/<int:pk>/delete/',
         views.StatusDeleteView.as_view(), name='delete_status'),

    # CRUD для типов
    path('dictionaries/type/add/',
         views.TypeCreateView.as_view(), name='add_type'),
    path('dictionaries/type/<int:pk>/edit/',
         views.TypeUpdateView.as_view(), name='edit_type'),
    path('dictionaries/type/<int:pk>/delete/',
         views.TypeDeleteView.as_view(), name='delete_type'),

    # CRUD для категорий
    path('dictionaries/category/add/',
         views.CategoryCreateView.as_view(), name='add_category'),
    path('dictionaries/category/<int:pk>/edit/',
         views.CategoryUpdateView.as_view(), name='edit_category'),
    path('dictionaries/category/<int:pk>/delete/',
         views.CategoryDeleteView.as_view(), name='delete_category'),

    # CRUD для подкатегорий
    path('dictionaries/subcategory/add/',
         views.SubCategoryCreateView.as_view(), name='add_subcategory'),
    path('dictionaries/subcategory/<int:pk>/edit/',
         views.SubCategoryUpdateView.as_view(), name='edit_subcategory'),
    path('dictionaries/subcategory/<int:pk>/delete/',
         views.SubCategoryDeleteView.as_view(), name='delete_subcategory'),

]