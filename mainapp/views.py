from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product, ProductCategory
from basketapp.models import Basket


def main(request):
    return render(request, 'mainapp/index.html', context={'user': request.user, 'items': ['item1', 'item2', 'item3']})


def products(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = {}
    if not request.user.is_anonymous:
        basket = Basket.objects.filter(user=request.user)

    if pk:
        if pk == '0':
            category = {'name': 'все'}
            products = Product.objects.all().order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }

        return render(request, 'mainapp/product_list.html', context)

    same_products = Product.objects.all()[1:3]

    context = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'basket': basket,
    }

    return render(request, 'mainapp/products.html', context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')
