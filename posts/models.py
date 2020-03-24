from django.db import models
import datetime
from datetime import datetime

objects = models.Manager()

def get_absolute_url(self):
    return "/post/%i/" % self.id

# Create your models here.
class blogPost(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=250, default="Description")
  author = models.CharField(max_length=200)
  date = models.DateTimeField(default=datetime.now, blank=True)
  content = models.TextField()
  id = models.IntegerField(primary_key=True)
