from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import signup, checkout
from .forms import LoginForm

app_name='accounts'

urlpatterns = [
    path('checkout/',checkout, name='checkout'),
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html',form_class=LoginForm),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]