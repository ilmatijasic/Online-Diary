from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("accounts/", views.accounts, name="accounts"),
    path("", include("django.contrib.auth.urls")),
    path("registration/", views.registration, name="registration"),
    path("folder/", views.folder_add, name="folder"),
    path("entry/", views.entry_add, name="entry"),
]