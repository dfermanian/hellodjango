from django.db import models

class User(models.Model):
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=200)

class Decision(models.Model):
	user = models.ForeignKey(User)
	position = models.IntegerField()

class Bucket(models.Model):
	decision = models.ForeignKey(Decision)
	name = models.CharField(max_length=200)
	image_url = models.CharField(max_length=200)
	position = models.IntegerField()

class Item(models.Model):
	bucket = models.ForeignKey(Bucket)
	name = models.CharField(max_length=200)
	position = models.IntegerField()

class Attribute(models.Model):
	item = models.ForeignKey(Item)
	name = models.CharField(max_length=200)
	field = models.CharField(max_length=1000)
	position = models.IntegerField()
	
