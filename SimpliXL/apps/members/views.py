from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from apps.accounts.models import CustomUser
from .models import FileUpload


# Create your views here.


@login_required
def home(request):
    return render(request, "members/dashboard.html")


class UserDetails(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = "members/profile.html"
    context_object_name = "profile"

    def get_queryset(self):
        email = self.request.user.email
        return CustomUser.objects.get(email=email)


class DeleteUser(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = "members/delete-confirm.html"
    success_url: reverse_lazy('accounts:login')

    def get_success_url(self):
        return reverse_lazy("accounts:login")


class UploadFilesView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = FileUpload
    fields = ('file_url',)
    template_name = "members/upload.html"
    success_url: reverse_lazy('members:home')

    success_message = "File Uploaded Successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.file_name = self.request.FILES["file_url"]
        return super(UploadFilesView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('members:home')


class UploadFilesHistory(LoginRequiredMixin, ListView):
    model = FileUpload
    template_name = "members/upload-history.html"
    context_object_name = "uploads"

    def get_queryset(self):
        id = self.request.user.id
        return FileUpload.objects.filter(user_id=id).order_by('-date_created')
