from django.urls import path, include
from . import views

app_name = 'mysite'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('about/', views.about_me, name='about_me'),
]