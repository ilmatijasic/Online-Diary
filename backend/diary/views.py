from django.http import HttpResponse
from django.contrib.auth.models import Permission, User
from django.shortcuts import render, get_object_or_404

from .models import Folder


def home(request):
    print(request.user.folder_set.all)
    folder = get_object_or_404(Folder)
    return render(request, "diary/home.html", {"folder": folder})


