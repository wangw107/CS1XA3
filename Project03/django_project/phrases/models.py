from django.db import models

class Phrases(models.Model):
	phrase = models.CharField(max_length=50)
	
