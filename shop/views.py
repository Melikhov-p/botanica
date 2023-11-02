from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Category, Product

def main(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/main.html',
                  {'chosen_category': category,
                   'categories': categories,
                   'products': products})


def contacts(request):
    return render(request, 'shop/contacts.html')


def about_us(request):
    return render(request, 'shop/about_us.html')


def admin_logout(request):
    logout(request)
    return redirect('shop:main_page')
