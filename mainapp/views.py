from django.shortcuts import render
from .models import Product


def main(request):
    return render(request, 'mainapp/index.html', context={'user': request.user, 'items': ['item1', 'item2', 'item3']})


def products(request, pk=None):
    if pk:
        print(pk)
    return render(request, 'mainapp/products.html', context={'products': Product.objects.all()})


def contacts(request):
    return render(request, 'mainapp/contacts.html')
