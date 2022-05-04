from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CommentForm
from .models import (About)


def main_page(request):
    form = CommentForm()
    about_user = About.objects.first()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for sending a message!')
            return redirect(request.path)

    return render(request, 'mysite/main.html', {
            'form': form,
            'about_user': about_user,
        }
    )


def about_me(request):
    form = CommentForm()
    about_user = About.objects.first()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for sending a message!')
            return redirect(request.path)

    return render(request, 'mysite/about.html', {
            'form': form,
            'about_user': about_user
        }
    )
