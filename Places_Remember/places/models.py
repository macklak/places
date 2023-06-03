
from django.contrib.gis.db import models
from allauth.socialaccount.models import SocialAccount
from django.contrib.gis.geos import Point


class memories(models.Model):
    name = models.CharField(max_length=100)
    comment =models.CharField()
    mapPlace=models.PointField(default=Point(0.0, 0.0))
    useruid=models.ForeignKey(SocialAccount ,on_delete=models.CASCADE)


