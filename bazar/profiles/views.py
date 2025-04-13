from django.shortcuts import render

def simple_profile_view(request):
    # Same hardcoded data
    context = {
        'user': {
            'first_name': 'Иван',
            'last_name': 'Иванов',
            'email': 'iiv1@tpu.ru',
        },
        'profileInfo': {
            'phone': '78999999999',
            'telegram': '@vanya',
            'dormitory': 'Общежитие № 14'
        }
    }
    return render(request, 'profile/profile.html', context)


def profile(request):
    return render(request, 'profile/profile.html')


def profile_products(request):
    products = [
        {'id': 1, 'name': 'Ноутбук', 'price': 45000, 'views': 12},
        {'id': 2, 'name': 'Смартфон', 'price': 25000, 'views': 8},
        {'id': 3, 'name': 'Наушники', 'price': 5000, 'views': 15},
    ]

    return render(request, 'profile/profileMyProduct.html', {'products': products})

def messages_list(request):
    messages = [
        {
            'id': 1,
            'sender': {'username': 'Иван Иванов'},
            'product': {'name': 'Ноутбук', 'price': 45000}
        },
        {
            'id': 2,
            'sender': {'username': 'Петр Петров'},
            'product': {'name': 'Смартфон', 'price': 25000}
        },
        {
            'id': 3,
            'sender': {'username': 'Сергей Сергеев'},
            'product': {'name': 'Наушники', 'price': 5000}
        }
    ]
    return render(request, 'profile/messages.html', {'messages': messages})

