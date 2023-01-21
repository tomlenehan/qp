import requests
from django.conf import settings
from django.db import models


class Bill(models.Model):
    bill_id = models.CharField(max_length=100)
    bill_type = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    congress = models.CharField(max_length=100)
    chamber = models.CharField(max_length=100)
    short_title = models.CharField(max_length=255)
    sponsor_id = models.CharField(max_length=100)
    sponsor_name = models.CharField(max_length=100)
    sponsor_party = models.CharField(max_length=100)
    sponsor_state = models.CharField(max_length=100)
    sponsor_uri = models.CharField(max_length=255)
    gpo_pdf_uri = models.CharField(max_length=255)
    congressdotgov_url = models.CharField(max_length=255)
    govtrack_url = models.CharField(max_length=255)
    introduced_date = models.CharField(max_length=100)
    active = models.BooleanField()
    last_vote = models.CharField(max_length=100)
    house_passage = models.CharField(max_length=100)
    senate_passage = models.CharField(max_length=100)
    enacted = models.CharField(max_length=100)
    vetoed = models.CharField(max_length=100)
    cosponsors = models.CharField(max_length=100)
    committees = models.CharField(max_length=100)
    primary_subject = models.CharField(max_length=100)
    summary = models.TextField()
    summary_short = models.TextField()

    def __str__(self):
        return self.short_title
