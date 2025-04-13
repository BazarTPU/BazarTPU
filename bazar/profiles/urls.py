from django.urls import path
from .views import simple_profile_view
from . import views

urlpatterns = [
    path('', simple_profile_view, name='profile'),
    path('', views.profile, name='profile'),
    path('products/', views.profile_products, name='profile_product'),
    path('messages/', views.messages_list, name='messages'),
]