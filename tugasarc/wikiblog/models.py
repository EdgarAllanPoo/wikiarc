from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    title_minor = models.CharField(max_length = 280)
    body = models.TextField(default = "Ini Isi")
    author = models.CharField(max_length = 60)
