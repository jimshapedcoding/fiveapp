from django.contrib import admin
from django.contrib.admin import ModelAdmin
from codingsession.models import CodingSession


@admin.register(CodingSession)
class CodingSessionAdmin(ModelAdmin):
    list_display = ['id', 'name', 'language', 'link', 'starting_time']
