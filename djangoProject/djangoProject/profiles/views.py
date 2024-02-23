from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from djangoProject.common.profile_helpers import get_profile
from djangoProject.profiles.models import Profile


class DetailProfileView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = "profiles/profile-details.html"

    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfileView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = "profiles/profile-delete.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()
