from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', context)


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', context)

def products(request):
    links_menu = [
            {
            'url': 'products',
            'title': 'Все'
            },

            {
            'url': 'products_home',
            'title': 'Дом'
            },

            {
            'url': 'products_office',
            'title': 'Офис'
            },

            {
            'url': 'products_modern',
            'title': 'Модерн'
            },

            {
            'url': 'products_classics',
            'title': 'Классика'
            }
        ]
    context = {
        'links_menu': links_menu,
        'title': 'Продукты'
    }
    return render(request, 'mainapp/products.html', context=context)



def products_home(request):
    context = {
        'links_menu': links_menu,
        'title': 'Продукты для дома'
    }
    return render(request, 'mainapp/products.html', context=context)


def products_office(request):
    context = {
        'links_menu': links_menu,
        'title': 'Продукты для офиса'
    }
    return render(request, 'mainapp/products.html', context=context)


def products_modern(request):
    context = {
        'links_menu': links_menu,
        'title': 'Продукты модерн'
    }
    return render(request, 'mainapp/products.html', context=context)


def products_classics(request):
    context = {
        'links_menu': links_menu,
        'title': 'Продукты классика'
    }
    return render(request, 'mainapp/products.html', context=context)