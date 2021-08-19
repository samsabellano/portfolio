from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CommentForm
from .models import (About)


def main_page(request):
    form = CommentForm()
    user_obj = User.objects.all()
    about_user = About.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for sending a message!')
            return redirect('/')

    return render(request, 'mysite/main.html',
        context = {
            'form': form,
            'user_obj': user_obj,
            'about_user': about_user,
        }
    )


def about_me(request):
    form = CommentForm()
    about_user = About.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for sending a message!')
            return redirect(request.path_info)

    return render(request, 'mysite/about.html',
        context = {
            'form': form,
            'about_user': about_user
        }
    )
