# Create your models here.
from django.db import models
from django.contrib.auth.models import User

import uuid


# Create your models here.
from idna import unicode


class Message(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    encrypted_message = models.CharField(max_length=200, null=True, blank=True)
    hashed_message = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.user_id)


#class DigitalCertificate(models.Model):
    #user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    #user_name = models.ForeignKey(User,on_delete=models.CASCADE)

    #def __unicode__(self):
        #return unicode(self.user_id)
