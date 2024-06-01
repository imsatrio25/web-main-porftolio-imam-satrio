from django.shortcuts import render

def index(request, *args, **kwargs):
    context = {}
    return render(request, 'index.html', context)

def second(request, *args, **kwargs):
    context = {}
    return render(request, 'imageclass.html', context)


