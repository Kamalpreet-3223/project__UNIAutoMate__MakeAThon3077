# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.contrib.auth.models import Group
from core.models import complains, roomRequest
from django.contrib import messages

admin.site.register(complains)

def accept(modeladmin, request, queryset):
    messages.add_message(request, messages.INFO, 'Okay! Following request have been accepted!')

accept.short_description = "Accept the Selected Orders"


def decline(modeladmin, request, queryset):
    messages.add_message(request, messages.INFO, 'The selected requests are declined!!')

decline.short_description = "Decline the Selected Orders"



@admin.register(roomRequest)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "roomNo", "PhoneNo", "TimeCleaning")
    actions = [accept,decline]


admin.site.site_header = "UAutoMate Admin Console"
admin.site.unregister(Group)
