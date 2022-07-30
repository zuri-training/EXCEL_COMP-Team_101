from django.urls import path
from . import views
from .views import CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

app_name = "base"
urlpatterns = [
    path("", views.home_page, name='home'),
    path('about/', views.about, name='about'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='base:login'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('authenticate/', views.authenticate, name='authenticate'),
]
