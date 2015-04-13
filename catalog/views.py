from django.shortcuts import render, get_object_or_404
from catalog.models import Category, Product

# Create your views here.


def index(request):
    page_title = 'Walkmart : Best Products'
    active_categories = Category.objects.filter(is_active=True)
    return render(request, 'catalog/index.html', locals())

def show_category(request, category_slug):
    c = get_object_or_404(Category, slug = category_slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    active_categories = Category.objects.filter(is_active=True)
    return render(request, 'catalog/category.html', locals())

def show_product(request, product_slug):
    p = get_object_or_404(Product, slug = product_slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    active_categories = Category.objects.filter(is_active=True)
    return render(request, 'catalog/product.html', locals())
