from django.db import models
from django.utils.timezone import now


class Type(models.Model):
    """Модель для хранения типов транзакций (Пополнение, Списание и тд.)."""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Status(models.Model):
    """Модель для хранения статусов транзакций (Бизнес, Личное и тд.)."""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    """Модель для хранения категорий, привязаных к определённому типу."""

    name = models.CharField(max_length=100)
    type = models.ForeignKey(
        Type, 
        on_delete=models.CASCADE,
        related_name='categories')

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    """Модель для хранения подкатегорий, привязанных к категории."""

    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        related_name='subcategories')

    def __str__(self):
        return self.name


class Transaction(models.Model):
    """Модель для хранения транзакций."""

    date = models.DateField(default=now, blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL, 
        null=True)
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.SET_NULL,
        null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.amount}"
