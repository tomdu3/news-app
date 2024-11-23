from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_news', views.add_news, name='add_news'),
]
