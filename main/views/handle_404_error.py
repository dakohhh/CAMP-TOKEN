from django.http import Http404
from django.shortcuts import render



def custom_404_view(request, exception=None):

    return render(request, '404.html', status=404)

