from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from .forms import MyGeoForm
from .models import memories


def index(request):
    return render(request,"places/index.html",{"Title": "Главная страница"})

def addmarker(request):
    if request.method == 'POST':
        form = MyGeoForm(request.POST)
        #form.useruid = request
        if form.is_valid():

            try:
                form.save()
            except:
                return render(request, 'places/profile.html', {"Title": "Профиль","form": form})

    else:
        form=MyGeoForm()
    return render(request,'places/profile.html',{"Title": "Профиль","form":form})



class MarkersMapView(TemplateView):
    template_name = "places/map.html"
