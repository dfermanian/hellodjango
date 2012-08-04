from django.db import models

class Customer(models.Model):
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	def __unicode__(self):
	        return self.email	

class Decision(models.Model):
	customer = models.ForeignKey(Customer)
	name = models.CharField(max_length=200)
	position = models.IntegerField()
	def __unicode__(self):
	        return self.customer.email + "; " + self.name

class Bucket(models.Model):
	decision = models.ForeignKey(Decision)
	name = models.CharField(max_length=200)
	image_url = models.CharField(max_length=1000)
	position = models.IntegerField()
	def __unicode__(self):
	        return self.decision.customer.email  + "; " + self.decision.name + "; " + self.image_url + "; " + self.name

class Item(models.Model):
	buckets = models.ManyToManyField(Bucket)
	name = models.CharField(max_length=200)
	position = models.IntegerField()
	image_url = models.TextField()
# 	image_url = models.CharField(max_length=1000)
	def __unicode__(self):
	        return self.bucket.decision.customer.email + "; " + self.bucket.decision.name + "; " + self.bucket.name + "; " + self.name

class Attribute(models.Model):
	item = models.ForeignKey(Item)
	name = models.CharField(max_length=200)
	field = models.CharField(max_length=1000)
	position = models.IntegerField()
	def __unicode__(self):
	        return self.item.bucket.decision.customer.email + "; " + self.item.bucket.decision.name + "; " + self.item.bucket.name + "; " + self.item.name + "; " + self.name
	
	
	
	
