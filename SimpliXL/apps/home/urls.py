from django.urls import path
from . import views

app_name = "base"
urlpatterns = [
    path("", views.home_page, name='home'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('authenticate/', views.authenticate, name='authenticate'),
]
