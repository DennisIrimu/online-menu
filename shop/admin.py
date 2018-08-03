from django.contrib import admin
from .models import Category,Food
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category, CategoryAdmin)

class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
admin.site.register(Product, ProductAdmin)
