from django.shortcuts import redirect

from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
# from django.contrib.auth.forms import UserCreationForm
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
