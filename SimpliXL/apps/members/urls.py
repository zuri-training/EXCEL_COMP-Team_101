from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.UserDetails.as_view(), name='profile'),
    path('delete/<int:pk>', views.DeleteUser.as_view(), name='delete'),
    path('upload/', views.UploadFilesView.as_view(), name='upload')
]
