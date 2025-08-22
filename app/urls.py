from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login.html/', views.login, name='login'),
    path('login.html/home.html/', views.home, name='home'),
    path('login.html/home.html/notes.html/', views.notes, name='notes'),
    path('login.html/home.html/account.html/', views.account, name='account'),
]