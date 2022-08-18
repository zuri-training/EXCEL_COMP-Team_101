from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView

from .views import CustomLoginView, RegisterPage, ResetPasswordCompleteView, ResetPasswordConfirmView, ResetPasswordDoneView, ResetPasswordView


app_name = 'accounts'

urlpatterns = [
    # Authentication System
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),

    # Password Reset
    path("password_reset/", ResetPasswordView.as_view(), name="password_reset"),
    path("password_reset/done/", ResetPasswordDoneView.as_view(),
         name="password_reset_done",),
    path("reset/<uidb64>/<token>/", ResetPasswordConfirmView.as_view(),
         name="password_reset_confirm",),
    path("reset/done/", ResetPasswordCompleteView.as_view(),
         name="password_reset_complete",),
]
