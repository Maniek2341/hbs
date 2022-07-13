from django.db import models


class Kontakt(models.Model):
    imie = models.CharField(max_length=50)
    email = models.EmailField()
    tresc = models.TextField(max_length=255)
