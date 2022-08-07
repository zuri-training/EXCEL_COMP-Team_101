from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from apps.accounts.models import CustomUser
from .models import FileUpload, EditedFileUpload

from django.conf import settings
import pathlib
import random
from apps.home import sample


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


def CorrectedFiles(request, file_sent):
    user = request.user
    correctedFile = EditedFileUpload.objects.create(
        user=user, file_url=f"corrected/document/{file_sent}", file_name=file_sent)

    correctedFile.save()


class UploadFilesView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    # Redirect Values
    actual_file_name, file_operation, file_extension, file_name = None, None, None, None

    model = FileUpload
    fields = ('file_url',)
    template_name = "members/upload.html"
    success_url: reverse_lazy('members:home')

    success_message = "File Uploaded Successfully"

    def form_valid(self, form):
        global actual_file_name, file_operation, file_extension, file_name

        file_operation = self.request.POST.get("operation")
        file_name = pathlib.Path(str(self.request.FILES.get("file_url"))).stem
        file_extension = pathlib.Path(
            str(self.request.FILES.get("file_url"))).suffix
        file_url_name = f"{file_name}_{random.randint(1000, 10000000)}{file_extension}"
        self.request.FILES["file_url"].name = file_url_name
        actual_file_name = self.request.FILES["file_url"]

        # Inserting records into the database
        form.instance.user = self.request.user
        form.instance.file_name = self.request.FILES["file_url"]
        form.instance.file_url = self.request.FILES["file_url"]

        return super(UploadFilesView, self).form_valid(form)

    def get_success_url(self):
        global actual_file_name, file_operation, file_extension, file_name
        sample.pan(actual_file_name, file_operation, file_extension, file_name)
        CorrectedFiles(self.request, actual_file_name)

        return reverse_lazy('members:home')


class UploadFilesHistory(LoginRequiredMixin, ListView):
    model = FileUpload
    template_name = "members/upload-history.html"
    context_object_name = "uploads"

    def get_queryset(self):
        id = self.request.user.id
        return FileUpload.objects.filter(user_id=id).order_by('-date_created')


def load_file(request, file_name):
    if request.method == 'GET':
        value = f"{settings.MEDIA_ROOT}/uploaded/document/{file_name}"

        data = sample.html_open_csv(value)

        return render(request, "members/panda.html", {"form": data})


# def download_file(request)

def highlight(request):
    content = {"form": sample.pan}

    return render(request, "members/sample.html", content)
