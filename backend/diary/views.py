from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Folder


def home(request):
    folder = get_object_or_404(Folder, pk="2")
    print(folder.entry_set.all())
    return render(request, "diary/home.html", {"folder": folder})
