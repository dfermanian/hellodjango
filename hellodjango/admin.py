from django.contrib import admin
from hellodjango.models import Decision, Customer, Bucket, Item, Attribute
from hellodjango.models import Customer

admin.site.register(Decision)
admin.site.register(Customer)
admin.site.register(Bucket)
admin.site.register(Item)
admin.site.register(Attribute)