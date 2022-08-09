from django.shortcuts import redirect

from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .forms import CustomUserCreationForm
from django.contrib.auth import login

from django.urls import reverse_lazy


# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('members:home')


class RegisterPage(FormView):
    template_name = 'accounts/register.html'
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
            success_url = reverse_lazy('members:home')
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('members:home')
        return super(RegisterPage, self).get(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('members:home')


class ResetPasswordView(PasswordResetView):
    success_url = reverse_lazy("accounts:password_reset_done")
    template_name = "password_reset/password_reset_form.html"

    # Email related template
    email_template_name = "password_reset/password_reset_email.html"
    subject_template_name = "password_reset/password_reset_subject.txt"


class ResetPasswordDoneView(PasswordResetDoneView):
    template_name = "password_reset/password_reset_done.html"


class ResetPasswordConfirmView(PasswordResetConfirmView):
    template_name = "password_reset/password_reset_confirm.html"
    success_url = reverse_lazy("accounts:password_reset_complete")


class ResetPasswordCompleteView(PasswordResetCompleteView):
    template_name = "password_reset/password_reset_complete.html"
