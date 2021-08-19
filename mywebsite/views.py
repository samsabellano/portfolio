from django.shortcuts import redirect


def redirect_main_page(request):
    return redirect('mysite:main_page', permanent=True)