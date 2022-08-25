import mimetypes
import os
import pathlib
import random
import uuid
import pandas as pd
import numpy as np

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, DeleteView, FormView,
                                       UpdateView)
from django.views.generic.list import ListView

from apps.accounts.models import CustomUser

from . import excel_logic
from .forms import UploadForm
from .models import EditedFileUpload, FileUpload, Profile,  TempTB

# Create your views here.


class uu(View):
    def get(self, request):
        form = UploadForm()

        return render(request, 'members/up.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = UploadForm(request.POST, request.FILES)
            if form.is_valid():
                uuu(request, form)
                # global actual_file_name, file_operation, file_extension, file_name

                # file_operation = self.request.POST.get("operation")
                # file_name = pathlib.Path(
                #     str(self.request.FILES.get("file_url"))).stem
                # file_extension = pathlib.Path(
                #     str(self.request.FILES.get("file_url"))).suffix
                # file_name = f"{file_name}_{random.randint(1000, 10000000)}{file_extension}"
                # file_url_name = f"{str(uuid.uuid4().hex)}_{random.randint(1000, 10000000)}{file_extension}"
                # self.request.FILES["file_url"].name = file_url_name
                # actual_file_name = self.request.FILES["file_url"]

                # # Inserting records into the database
                # form.instance.user = self.request.user
                # form.instance.file_name = file_name
                # form.instance.file_url = self.request.FILES["file_url"]

                # form.save()
                # return JsonResponse({'data': 'Data uploaded'})
                return uuu(request, form)
                # return JsonResponse({'data': form})

            else:
                return JsonResponse({'data': 'Something went wrong!!'})


class uuu(CreateView):
    model = TempTB
    fields = ('file_url',)
    success_url: reverse_lazy('members:home')

    def form_valid(self, form):
        # file_operation = self.request.POST.get("operation")
        file_name = pathlib.Path(
            str(self.request.FILES.get("file_url"))).stem
        file_extension = pathlib.Path(
            str(self.request.FILES.get("file_url"))).suffix
        file_name = f"{file_name}_{random.randint(1000, 10000000)}{file_extension}"
        file_url_name = f"{str(uuid.uuid4().hex)}_{random.randint(1000, 10000000)}{file_extension}"
        self.request.FILES["file_url"].name = file_url_name
        actual_file_name = self.request.FILES["file_url"]

        # # Inserting records into the database
        form.instance.user = self.request.user
        form.instance.file_name = file_name
        form.instance.file_url = self.request.FILES["file_url"]

        form.save()

        return JsonResponse({'data': file_url_name})

    def get_success_url(self):
        return reverse_lazy('members:home')


def color_dupes(x):
    c1 = 'background-color:red'
    c2 = ''
    cond = x.stack().duplicated(keep=False).unstack()
    df1 = pd.DataFrame(np.where(cond, c1, c2),
                       columns=x.columns, index=x.index)
    return df1
    # if df has many columns: df.style.apply(color_dupes,axis=None,subset=['A','B'])


# def cc(s):
#     is_max = s == s.max()
#     return ['background-color: red' if v else '' for v in is_max]
#     color = 'red' if x < 2 else 'black'
#     return 'color: %s' % color

def cc(s, dup):
    for i in s:
        if i in dup:
            return ['background-color: red']
        else:
            pass


@login_required
def load_file(request, actual_file_name):
    actual_file = f"{settings.MEDIA_ROOT}/temp/{actual_file_name}"

    file_name = pathlib.Path(str(actual_file_name)).stem
    file_extension = pathlib.Path(str(actual_file_name)).suffix
    data = None

    if file_extension == ".csv":
        data = pd.read_csv(actual_file)

    elif file_extension == ".xls" or file_extension == ".xlsx":
        data = pd.read_excel(actual_file)

    dup = data.drop_duplicates().to_html()

    dupli = data[data.duplicated(keep=False)].index.values
    # data = data.style.apply(lambda x: [
    #                         'background:green; color:#fff;' if i not in dupli else '' for i in x])
    data = data.style.apply(
        lambda x: ['background:red; color:#fff;' if x.name in dupli else '' for i in x], axis=1)
    exp = data.to_excel("sample.xlsx", engine='openpyxl')
    data = data.to_html()

    return render(request, "members/spreadsheet.html", {'form': data, 'form1': dup})


@login_required
def home(request):
    FinishedFiles = EditedFileUpload.objects.filter(user=request.user)
    return render(request, "members/dash.html", {'form': FinishedFiles})


@login_required
def tools(request):
    return render(request, "members/tools.html")


@login_required
def welcome(request):
    return render(request, "members/welcome_dash.html")


@login_required
def dash_history(request):
    return render(request, "members/dashboard-tour.html")


@login_required
def dash_history3(request):
    return render(request, "members/dashboard-tour3.html")


@login_required
def dash_tour4(request):
    return render(request, "members/dash-tour4.html")


@login_required
def dash_tour5(request):
    return render(request, "members/dashboardtour5.html")


@login_required
def dash_tour1(request):
    return render(request, "members/tour1.html")


@login_required
def dash_tour2(request):
    return render(request, "members/tour2.html")


@login_required
def dash_tour3(request):
    return render(request, "members/tour3.html")


@login_required
def profile_dash(request):
    return render(request, "members/profile-dash.html")


@login_required
def upload_one(request):
    return render(request, "members/upload-onefile.html")


@login_required
def upload_two(request):
    return render(request, "members/upload-twofiles.html")


@login_required
def upload_files(request):
    return render(request, "members/uploading-page-twofiles.html")


@login_required
def upload_file(request):
    return render(request, "members/uploading-page.html")


@login_required
def file_upload(request):
    return render(request, "members/FileUpload.html")


class UserDetails(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = "members/profile.html"
    context_object_name = "profile"

    def get_queryset(self):
        email = self.request.user.email
        return CustomUser.objects.get(email=email)


class UpdateUser(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ["full_name", ]
    template_name = "members/profile-dash.html"
    success_url: reverse_lazy('members:home')

    def get_success_url(self):
        return reverse_lazy("members:home")


class DeleteUser(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = "members/delete-confirm.html"
    success_url: reverse_lazy('accounts:login')

    def get_success_url(self):
        return reverse_lazy("accounts:login")


@login_required
def setting(request):
    # user_profile = Profile.objects.filter(user=request.user)

    # if user_profile:
    # if request.method == 'POST':
    #     if request.FILES.get('image') == None:
    #         image = user_profile.profileimg
    #         company = request.POST['company']
    #         location = request.POST['location']

    #         user_profile.profileimg = image
    #         user_profile.company = company
    #         user_profile.location = location
    #         user_profile.save()

    #     elif request.FILES.get('image') != None:
    #         image = request.FILES.get('image')
    #         company = request.POST['company']
    #         location = request.POST['location']

    #         user_profile.profileimg = image
    #         user_profile.company = company
    #         user_profile.location = location
    #         user_profile.save()

    #     return redirect('settings')
    # return render(request, 'members/settings.html', {'user_profile': user_profile})
    # return render(request, 'members/settings.html')
    pass


@login_required
def CorrectedFiles(request, file_sent, file_name):
    user = request.user
    correctedFile = EditedFileUpload.objects.create(
        user=user, file_url=f"corrected/document/{file_sent}", file_name=file_name)

    correctedFile.save()


class UploadFilesView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    # Redirect Values
    actual_file_name, file_operation, file_extension, file_name = None, None, None, None

    model = FileUpload
    fields = ('file_url',)
    template_name = "members/upload.html"
    success_url: reverse_lazy('members:corrected')

    success_message = "File Uploaded Successfully"

    def form_valid(self, form):
        global actual_file_name, file_operation, file_extension, file_name

        file_operation = self.request.POST.get("operation")
        file_name = pathlib.Path(str(self.request.FILES.get("file_url"))).stem
        file_extension = pathlib.Path(
            str(self.request.FILES.get("file_url"))).suffix
        file_name = f"{file_name}_{random.randint(1000, 10000000)}{file_extension}"
        file_url_name = f"{str(uuid.uuid4().hex)}_{random.randint(1000, 10000000)}{file_extension}"
        self.request.FILES["file_url"].name = file_url_name
        actual_file_name = self.request.FILES["file_url"]

        # Inserting records into the database
        form.instance.user = self.request.user
        form.instance.file_name = file_name
        form.instance.file_url = self.request.FILES["file_url"]

        return super(UploadFilesView, self).form_valid(form)

    def get_success_url(self):
        global actual_file_name, file_operation, file_extension, file_name
        excel_logic.pan(actual_file_name, file_operation,
                        file_extension, file_name)
        CorrectedFiles(self.request, actual_file_name, file_name)

        return reverse_lazy('members:corrected')


class UploadFilesHistory(LoginRequiredMixin, ListView):
    model = FileUpload
    template_name = "members/upload-history.html"
    context_object_name = "uploads"

    def get_queryset(self):
        id = self.request.user.id
        return FileUpload.objects.filter(user_id=id).order_by('-date_created')


class UploadDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = FileUpload
    template_name = "members/deleteFileHistory.html"
    success_url: reverse_lazy('members:upload-history')
    success_message = "File Deleted Successfully"

    def form_valid(self, form):
        file_url = self.get_object().file_url
        os.unlink(f"{settings.MEDIA_ROOT}/{file_url}")
        return super(UploadDeleteView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy("members:upload-history")


class CorrectedFilesView(LoginRequiredMixin, ListView):
    model = EditedFileUpload
    template_name = "members/corrected.html"
    context_object_name = "uploads"

    def get_queryset(self):
        id = self.request.user.id
        return EditedFileUpload.objects.filter(user_id=id).order_by('-date_created')


class CorrectedDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = EditedFileUpload
    template_name = "members/deleteFileHistory.html"
    success_url: reverse_lazy('members:corrected')
    success_message = "File Deleted Successfully"

    def form_valid(self, form):
        file_url = self.get_object().file_url
        os.unlink(f"{settings.MEDIA_ROOT}/{file_url}")
        return super(CorrectedDeleteView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy("members:corrected")


@login_required
def download_file(request, file_name):
    # fill these variables with real values
    file_path = f"{settings.MEDIA_ROOT}/{file_name}"

    fileHandle = open(file_path, 'rb')
    mime_type, _ = mimetypes.guess_type(file_path)
    response = HttpResponse(fileHandle, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % file_name
    return response


@login_required
def highlight(request):
    content = {"form": excel_logic.pan}

    return render(request, "members/sample.html", content)
