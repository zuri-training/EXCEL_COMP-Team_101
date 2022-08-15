from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('', views.home, name='home'),

    # settings urls
    path('settings/', views.setting, name='settings'),
    path('tools/', views.tools, name='tools'),
    path('profile-dashboard/', views.profile_dash, name='profile_dash'),

    path('welcome-dashboard/', views.welcome, name='welcome'),
    path('tour/', views.dash_tour1, name='tour'),



    path('upload-file/', views.upload_file, name='upload_file'),

    path('upload-files/', views.upload_files, name='upload_files'),
    path('upload-one/', views.upload_one, name='upload_one'),
    path('upload-two/', views.upload_two, name='upload_two'),
    path('FileUpload/', views.file_upload, name='file_upload'),



    # User Profile Urls
    path('profile/', views.UserDetails.as_view(), name='profile'),
    path('delete/<int:pk>', views.DeleteUser.as_view(), name='delete'),

    # File Upload Urls
    path('up/', views.uu.as_view(), name='upload'),
    path('ff/', views.uuu.as_view(), name='displays'),
    #     path("aa/", .as_view(), name="")

    #     path('upload/', views.UploadFilesView.as_view(), name='upload'),
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


    path('file/<str:actual_file_name>', views.load_file, name='file'),
    path('sample/', views.highlight, name='highlight')
]
