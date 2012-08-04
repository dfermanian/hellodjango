from django.http import HttpResponse

from hellodjango.models import Customer, Decision, Bucket, Item, Attribute
from django.shortcuts import render

import json

def savebuckets(request):
	json = request.POST.get("name")
	data = json.loads(json);
	for decision in data:
		d = Decision.objects.get(id=decision.id)
		d.name = decision.name
		d.position = decision.position
		d.save()
		for bucket in decisions.buckets:
			b = Bucket.objects.get(id=bucket.id)
			b.name = bucket.name
			b.position = bucket.position
			b.image_url = bucket.image_url
			b.save()
			for item in bucket.items:
				i = Item.objects.get(id=item.id)
				i.name = item.name
				i.position = item.position
				i.save()
				for attribute in item.attributes:
					a = Attribute.objects.get(id = attribute.id)
					a.name = attribute.name
					a.position = attribute.position
					a.save()
		
def moveitem(request):
	data = json.loads(request.raw_post_data)['list'];
	for item in data:
		i = Item.objects.get(id=item["id"])
		i.position = item["position"]
		i.save()
	return HttpResponse("OK")

		
def copyitem(request):
	item = json.loads(request.raw_post_data);
	i = Item.objects.get(id=item["item_id"])
	b = Bucket.objects.get(id=item["bucket_id"])
	i.buckets.add(b)
	i.save()
	return HttpResponse("OK")
	
		
def additem(request):
	data = json.loads(request.raw_post_data)['list'];
	for item in data:
		new_id = len(Item.objects.all()) + 1
		parent_bucket = Bucket.objects.get(id=item["bucket_id"])
		i = Item(new_id, item["name"], item["position"], item["image_url"])
		i.buckets.add(parent_bucket)
		i.save()
	return HttpResponse("OK")	

def addbucket(request):
	item = json.loads(request.raw_post_data);
	
	








