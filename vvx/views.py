from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Home view renders the main page of the application.
def home_view(request):
    context = {}
    return render(request, 'vvx/index.html', context)