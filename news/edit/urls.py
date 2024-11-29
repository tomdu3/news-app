from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_news', views.add_news, name='add_news'),
    path('edit_news/<int:id>', views.edit_news, name='edit_news'),
]
