from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    #     path('', views.template, name='home'),

    path('', views.home, name='home'),

    # settings urls
    path('settings/', views.setting, name='settings'),
    path('tools/', views.tools, name='tools'),
    path('tour/', views.dash_history, name='tour'),
    path('newuserfile/', views.newuserfile, name='newuser'),
    path('existing-dashboard/', views.exist, name='exist'),
    path('profile-dashboard/', views.profile_dash, name='profile_dash'),

    path('existing-dash1/', views.dash_tour1, name='tour1'),
    path('existing-dash2/', views.dash_tour2, name='tour2'),
    path('existing-dash3/', views.dash_history3, name='tour3'),
    path('existing-dash3a/', views.dash_tour3, name='tour3a'),
    path('existing-dash4/', views.dash_tour4, name='tour4'),
    path('existing-dash5/', views.dash_tour5, name='tour5'),

    path('upload-file/', views.upload_file, name='upload_file'),
    path('upload-files/', views.upload_files, name='upload_files'),
    path('upload-one/', views.upload_one, name='upload_one'),
    path('upload-two/', views.upload_two, name='upload_two'),
    path('FileUpload/', views.file_upload, name='file_upload'),


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
