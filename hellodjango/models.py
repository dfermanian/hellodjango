from django.db import models

class Bucket:
	name = models.CharField(max_length=200)
	