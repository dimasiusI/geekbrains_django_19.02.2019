from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html', context={'name': 'ivan', 'items': ['item1', 'item2', 'item3']})


def products(request):
    return render(request, 'mainapp/products.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')
