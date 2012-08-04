from django.http import HttpResponse

from hellodjango.models import Decision, Bucket
from django.shortcuts import render




def decisions_view(request):
	count = len(Decision.objects.all())
	html = "<html> <body> There are %s decisions.</body></html>" % count
	return HttpResponse(html)

def decisions_view(request, decision_id):
	d = Decision.objects.get(pk=decision_id)
	html = "<html> <body>%s</body></html>" % d
	return HttpResponse(html)

#def buckets_view(request, decision_id):
#	count = len(Bucket.objects.all())
#	html = "<html> <body> There are %s buckets.</body></html>" % count
#	return HttpResponse(html)

def buckets_view(request, decision_id):
	#Bucket.objects.filter(decision_id=1).get(position=1)
	buckets = Bucket.objects.filter(decision_id=decision_id)
	templateValues = {'buckets' : buckets }
	return render(request, 'bucketsTemplate.html', templateValues)