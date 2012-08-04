from django.http import HttpResponse

from hellodjango.models import Customer, Decision, Bucket, Item, Attribute
from django.shortcuts import render

def customer_view(request, customer_id):
	decisions = Decision.objects.filter(customer_id = customer_id)
	buckets = None
	for decision in decisions:
		buckets = Bucket.objects.filter(decision_id=decision.decision_id)
		items_map = None
		for bucket in buckets:
			i = Item.objects.filter(bucket_id = bucket.bucket_id)
			for item in i:
				items.append(Attribute.objects.filter(item_id = i.item_id))

				

def decision_view(request, decision_id):
	buckets = Bucket.objects.filter(decision_id=decision_id)
	templateValues = {'buckets' : buckets }
	return render(request, 'bucketsTemplate.html', templateValues)

def bucket_view(request, bucket_id):
	#Bucket.objects.filter(decision_id=1).get(position=1)
	items = Item.objects.filter(bucket_id=bucket_id)
	templateValues = {'items' : items }
	return render(request, 'itemsTemplate.html', templateValues)

def item_view(request, item_id):
	attributes = Attributes.objects.filter(item_id=item_id)
	templateValues = {'attributes' : attributes}
	return render()
	

#def buckets_view(request, decision_id):
#	count = len(Bucket.objects.all())
#	html = "<html> <body> There are %s buckets.</body></html>" % count
#	return HttpResponse(html)
