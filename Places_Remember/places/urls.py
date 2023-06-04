from django.urls import path
from .views import *

urlpatterns =[
    path("",index,name="home"),
    #path("accounts/profile/",profile,name="profile"),
    path("accounts/profile/",addmarker,name="profile"),
    path("map/", MarkersMapView.as_view()),

]