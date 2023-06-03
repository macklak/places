from django.contrib.gis import forms
from django.contrib.gis.geos import Point


from .models import memories

class MyGeoForm(forms.ModelForm):
    name=forms.CharField(max_length=100)
    comment=forms.CharField()
    mapPlace= forms.PointField(widget=
        forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}),initial=Point(0.0,0.0))
    class Meta:
        model=memories
        fields = ["name","comment","mapPlace"]