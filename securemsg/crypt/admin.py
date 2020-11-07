from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import DigitalCertificate, Message
# Register your models here.

admin.site.register(DigitalCertificate)
admin.site.register(Message)