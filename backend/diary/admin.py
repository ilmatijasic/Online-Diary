from django.contrib import admin

from .models import Entry, Folder

admin.site.register(Entry)
admin.site.register(Folder)