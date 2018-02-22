from django.db import models

class Search(models.Model):
    query = models.CharField(max_length=1024)

