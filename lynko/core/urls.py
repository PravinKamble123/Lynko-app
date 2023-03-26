from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *

app_name='core'

urlpatterns = [
    path('', login_required(index), name='index'),
    path('about/', about, name='about'),
    path('pricing/', pricing, name='pricing'),
]