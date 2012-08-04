from django.http import HttpResponse

from hellodjango.models import Decision, Bucket, Item
from django.shortcuts import render




def decisions_view(request, decision_id):
	buckets = Bucket.objects.filter(decision_id=decision_id)
	templateValues = {'buckets' : buckets }
	return render(request, 'bucketsTemplate.html', templateValues)
	

#def buckets_view(request, decision_id):
#	count = len(Bucket.objects.all())
#	html = "<html> <body> There are %s buckets.</body></html>" % count
#	return HttpResponse(html)

def buckets_view(request, bucket_id):
	#Bucket.objects.filter(decision_id=1).get(position=1)
	items = Item.objects.filter(bucket_id=bucket_id)
	templateValues = {'items' : items }
	return render(request, 'itemsTemplate.html', templateValues)