from django.shortcuts import render
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin

from LittleSportsBiscuit.models import Coach, Conference, Player, Roster, Schedule, Sport, Team

# Create your views here.


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"


class ConferencesView(TemplateView):
    template_name = "conferences.html"

    def get_context_data(self, **kwargs):
        context = super(ConferencesView, self).get_context_data(**kwargs)