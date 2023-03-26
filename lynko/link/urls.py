from django.urls import path

from .views import *

app_name = 'link'

urlpatterns =[
    path('create-category/', create_category, name='create_category'),
    path('create-link/', create_link, name='create_link'),
    path('<int:pk>/edit/', edit_link, name='edit'),
    path('<int:pk>/delete/', delete_link, name='delete'),
    path('categories/<int:pk>/edit/', edit_category, name='edit_category'),
    path('categories/<int:pk>/delete/', delete_category, name='delete_category'),
   
]