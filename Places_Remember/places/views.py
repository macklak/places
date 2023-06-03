from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from .forms import MyGeoForm
from .models import memories


def index(request):
    return render(request,"places/index.html",{"Title": "Главная страница"})
def profile(request):
    return render(request,"places/profile.html",{"Title": "Профиль"})
def addmarker(request):
    if request.method == 'POST':
        form = MyGeoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                return render(request, 'places/profile.html', {"form": form})

    else:
        form=MyGeoForm()
    return render(request,'places/profile.html',{"form":form})

class contanctForm(FormView):
    template_name = 'places/profile.html'
    form_class = MyGeoForm
    success_url = '/'
    def form_valid(self, form):
        memories.objects.create(**form.cleaned_data)
        return super().form_valid(form)

class MarkersMapView(TemplateView):
    template_name = "places/map.html"
