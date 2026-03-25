from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home(request):
    return render(request, "core/home.html")


@login_required
def profile(request):
    attributes = request.session.get("attributes", {})
    return render(
        request,
        "core/profile.html",
        {
            "cas_attributes": attributes,
        },
    )