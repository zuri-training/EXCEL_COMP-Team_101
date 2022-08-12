from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('', views.home, name='home'),
    # settings urls
    path('setting/', views.setting, name='setting'),
    path('tools/', views.tools, name='tools'),
    path('tour/', views.dash_history, name='tour'),
    path('existing-dashboard/', views.exist, name='exist'),
    path('welcome-dashboard/', views.welcome, name='welcome'),
    # User Profile Urls
    path('profile/', views.UserDetails.as_view(), name='profile'),
    path('delete/<int:pk>', views.DeleteUser.as_view(), name='delete'),

    # File Upload Urls
    path('upload/', views.UploadFilesView.as_view(), name='upload'),
    path('upload-history/', views.UploadFilesHistory.as_view(),
         name='upload-history'),
    path('upload-delete/<int:pk>/',
         views.UploadDeleteView.as_view(), name='upload-delete'),

    # Corrected Result Url
    path("corrected/", views.CorrectedFilesView.as_view(), name="corrected"),
    path('delete-corrected/<int:pk>/',
         views.CorrectedDeleteView.as_view(), name='delete-corrected'),

    #  General file operation
    path('download-file/<path:file_name>/',
         views.download_file, name="download-file"),


    path('file/<str:file_name>', views.load_file, name='file'),
    path('sample/', views.highlight, name='highlight')
]
