from django.contrib import admin
from .models import Category,Food
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    #prepopulated_fields = {'slug': ('name')}
admin.site.register(Category, CategoryAdmin)

class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    #prepopulated_fields = {'slug': ('name')}
admin.site.register(Food, FoodAdmin)
