from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CodeTemplate(models.Model):
    name = models.CharField(max_length=128, unique=True)
    code = models.TextField()
    screenshot = models.ImageField(upload_to='screenshot', blank=True)

    def __unicode__(self):
        return self.name

class DownloadCodes(models.Model):
    name = models.ForeignKey(CodeTemplate)

    def __unicode__(self):
        return self.name
    
class UserProfile(models.Model):
    # this line is req. links userprofile to a user model instance
    user = models.OneToOneField(User)
    
    # additional attributes
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_image', blank=True)
    
    # unicode stuf
    def __unicode__(self):
        return self.user.username
