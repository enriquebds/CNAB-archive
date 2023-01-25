from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadArchiveForm
from .models import UploadArchive, Cnab

# Create your views here.
def upload(req):

    if req.method == "POST":
        form = UploadArchive(req.POST, req.Files)
        file = req.Files["file"]

        archive = UploadArchive.objects.create(archive=file)
        archive.save()

        list = []
        with open(f"uploads/{str(archive.archive)}", encoding="utf-8") as read:
             for line in read:
                list.append(line)
