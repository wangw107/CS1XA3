from django.db import models

class Phrases(models.Model):
	phrase = models.CharField(max_length=50, unique=True)
class Sentences(models.Model):
        sentence = models.CharField(max_length=256, unique=True)
