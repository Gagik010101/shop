from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register),
    path('signIn', views.signIn),
    path('profile', views.profile),
    path('addProduct', views.addProduct),
    path('getProduct', views.getProduct),
    path('getCategory', views.getCategory),
    path('getCountry', views.getCountry),
    path('getProduct/<int:id>', views.getProductById),
    path('logout_user', views.logout_user)
]
