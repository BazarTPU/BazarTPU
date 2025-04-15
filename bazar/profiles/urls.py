from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('products/', views.profile_products, name='profile_product'),
    path('messages/', views.messages_list, name='messages'),
    path('profile/update/', views.update_profile, name='update_profile'),
]