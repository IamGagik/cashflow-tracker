from django.contrib import admin
from .models import Status, Type, Category, SubCategory, Transaction

admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Transaction)
