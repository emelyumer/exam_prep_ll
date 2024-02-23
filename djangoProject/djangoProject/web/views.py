from django.shortcuts import render, redirect

from djangoProject.albums.models import Album
from djangoProject.common.profile_helpers import get_profile
from djangoProject.web.forms import CreateProfileForm



def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form": form,
        "without_user": True
    }
    return render(request, "web/home-no-profile.html", context)


def index(request):
    profile = get_profile()

    if profile is None:
        return create_profile(request)

    context = {
        "albums": Album.objects.all(),
    }

    return render(request, "web/home-with-profile.html", context)
