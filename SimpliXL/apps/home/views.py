from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.urls import reverse_lazy

from django.shortcuts import render, redirect


# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'home/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('base:home')


class RegisterPage(FormView):
    template_name = 'home/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
            success_url = reverse_lazy('base:home')
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('base:home')
        return super(RegisterPage, self).get(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('base:home')


def home_page(request):
    return render(request, "home/index.html")


def about(request):
    return render(request, 'home/about.html')


@login_required
def dashboard(request):
    return render(request, 'home/dashboard.html')


@login_required
def authenticate(request):
    return render(request, 'home/authenticate.html')
