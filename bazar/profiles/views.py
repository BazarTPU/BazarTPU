from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse

@login_required
def profile(request):
    context = {
        'user': request.user, #django User model уже содержит базовые поля, включая дату регистрации
        'profileInfo': {
            'phone': request.user.phone,
            'telegram': request.user.telegram,
            'dormitory': request.user.dormitory,
        }
    }
    return render(request, 'profile/profile.html', context)

@login_required
def update_profile(request):
    if request.method == "POST":
        user = request.user

        # обновляем только разрешенные поля
        user.phone = request.POST.get("phone", user.phone)
        user.telegram = request.POST.get("telegram", user.telegram)
        user.dormitory = request.POST.get("dormitory", user.dormitory)

        try:
            user.save()
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Метод не POST"})


@login_required
def profile_products(request):
    # здесь должна быть логика объявлений
    products = [
        {'id': 1, 'name': 'Ноутбук', 'price': 45000, 'views': 12},
        {'id': 2, 'name': 'Смартфон', 'price': 25000, 'views': 8},
        {'id': 3, 'name': 'Наушники', 'price': 5000, 'views': 15},
    ]
    return render(request, 'profile/profileMyProduct.html', {'products': products})

@login_required
def messages_list(request):
    # здесь должна быть логика получения сообщений пользователя
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
