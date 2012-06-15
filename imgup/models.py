from django.db import models
from django.contrib.auth.models import User
import os
from imgupload.settings import *

class Img(models.Model):
    img_name = models.CharField(max_length=80)
    uploader = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.img_name
    
    def get_absolute_url(self):
        return os.path.join(STATIC_URL,self.img_name)