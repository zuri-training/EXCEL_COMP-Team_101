from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

from .views import CustomLoginView, RegisterPage


app_name = 'accounts'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),
]
