from django.shortcuts import render


def index(request):
  context_dict = {'name': 'Andrea'}
  return render(request, 'index.html',  context_dict)
