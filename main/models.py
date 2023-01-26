import requests
from django.conf import settings
from django.db import models


class Bills(models.Model):
    number = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=1000)
    congress = models.CharField(max_length=10)
    latest_action_date = models.DateField()
    latest_action_text = models.TextField()
    origin_chamber = models.CharField(max_length=10)
    origin_chamber_code = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    update_date = models.DateField()
    url = models.URLField()
    text_url = models.URLField(null=True)
    summary = models.TextField(null=True)

    def __str__(self):
        return self.title


class Members(models.Model):
    bioguide_id = models.CharField(max_length=10, unique=True)
    district = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    party = models.CharField(max_length=255)
    chamber = models.CharField(max_length=255, null=True)
    start_date = models.CharField(max_length=10,null=True)
    end_date = models.CharField(max_length=10,null=True)
    state = models.CharField(max_length=255)
    url = models.URLField(null=True)
    image_url = models.URLField(null=True)

    def __str__(self):
        return self.name


class BillSponsors(models.Model):
    bill = models.ForeignKey(Bills, on_delete=models.CASCADE)
    member = models.ForeignKey(Members, on_delete=models.CASCADE)
