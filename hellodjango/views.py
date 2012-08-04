from django.http import HttpResponse

from hellodjango.models import Customer, Decision, Bucket, Item, Attribute
from django.shortcuts import render

# ORDER ALL BY POSITION!

def customer_view(request, customer_id):
	filtered_decisions = sorted(Decision.objects.filter(customer_id = customer_id), key=lambda Decision: Decision.position)
	decisions = []
	for decision in filtered_decisions:
		filtered_buckets = sorted(Bucket.objects.filter(decision_id = decision.id), key=lambda Bucket: Bucket.position)
		buckets = []
		for bucket in filtered_buckets:
			filtered_items = sorted(Item.objects.filter(bucket_id = bucket.id), key=lambda Item: Item.position)
			items = []
			for item in filtered_items:
				filtered_attributes = sorted(Attribute.objects.filter(item_id = item.id), key=lambda Attribute: Attribute.position)
				attributes = []
				for attribute in filtered_attributes:
					attributes.append( {"name" : attribute.name, "field" : attribute.field, "id" : attribute.id } )
				items.append({"attributes" : attributes, "name" : item.name, "id" : item.id })
			buckets.append({"items" : items, "name" : bucket.name, "image_url" : bucket.image_url, "id" : bucket.id})	
		decisions.append({"buckets" : buckets, "name" : decision.name, "id" : decision.id })
	templateValues = {"decisions" : decisions, "id" : customer_id }
	return render(request, 'bucketsTemplate.html', templateValues)
	

"""
buckets = [{"items": [{"attributes": [{"name": name, "string": string}],
						"name": name,
						}]
			"name": name,



			}]			
"""	

def decision_view(request, decision_id):
	print "!!!!!!decision_view!!!!!!!!"
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
