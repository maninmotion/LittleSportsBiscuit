from django.contrib import admin

# Register your models here.
"""
This module provides useful django admin hooks that allow you to manage
various components through the django admin panel (if enabled).
"""

from django.contrib import admin

from .models import Conference, Team, Coach, Player, Roster, Schedule, Sport


class CallerAdmin(admin.ModelAdmin):
    """This class provides admin panel integration for our
    :class:`django_twilio.models.Caller` model.
    """
    list_display = ('__str__', 'blacklisted')


admin.site.register(Conference)
admin.site.register(Team)
admin.site.register(Coach)
admin.site.register(Player)
admin.site.register(Roster)
admin.site.register(Schedule)
admin.site.register(Sport)