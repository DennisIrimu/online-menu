from django.shortcuts import render, get_object_or_404
from .models import Category,Food
# Create your views here.
def food_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    foods = Food.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        foods = foods.filter(category=category)
    return render(request,'shop/food/list.html',{'category':category,'categories':categories,'foods':foods})

def food_detail(request, id, slug):
    food = get_object_or_404(Product,id=id,slug=slug,available=True)
    return render(request,'shop/food/detail.html',{'food':food})
