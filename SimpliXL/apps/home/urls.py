from django.urls import path
from . import views

app_name = "base"
urlpatterns = [
    path("", views.home_page, name='home'),
    path('about/', views.about, name='about'),
    path('feature/', views.feature, name='feature'),
    path('how_to/', views.how_to, name='how_to'),
    path('terms/', views.terms, name='terms'),
    path('request_tool/', views.request_tool, name='request'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('authenticate/', views.authenticate, name='authenticate'),
]
