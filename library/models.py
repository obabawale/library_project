from django.db import models

class Book(models.Model):
	name = models.CharField(max_length=32)
	isbn = models.CharField(max_length=12)
	author = models.CharField(max_length=32)
