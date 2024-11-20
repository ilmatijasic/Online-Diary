from django.http import HttpResponse
from django.contrib.auth.models import Permission, User
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login

from .models import Folder
from .forms import RegistrationForm, FolderForm, EntryForm


def home(request):
    # print(request.user.folder_set.all)
    # folder = get_object_or_404(Folder)
    return render(request, "diary/home.html")


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")

    else:
        form = RegistrationForm()

    return render(request, "registration/registration.html", {"form": form})

def folder_add(request):
    if request.method == "POST":
        form = FolderForm(request.POST)

        if form.is_valid():
            folder = form.save(commit=False)
            folder.user = request.user
            folder.save()
            return redirect("/")

    else:
        form = FolderForm()

    return render(request, "diary/folder_add.html", {"form": form})

def entry_add(request):
    if request.method == "POST":
        form = EntryForm(request.POST)

        if form.is_valid():
            # print(form.user)
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect("/")

    else:
        form = EntryForm()

    return render(request, "diary/entry_add.html", {"form": form})

