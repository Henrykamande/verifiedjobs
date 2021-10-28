from django.db import models
import uuid

from django.db.models.base import Model
from users.models import Profile
# Create your models here.


#use as jobs


class Project(models.Model):
    owner=models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    title= models.CharField(max_length=200)
    description= models.TextField(null=True, blank=True)
    featured_image= models.ImageField(null=True, blank=True, default='default.jpg')
    created =models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)
    salary=models.FloatField(null=True)
    countries= models.ManyToManyField('Countries', blank=True ) 
    description= models.TextField(null=True, blank=True)
    requirements= models.TextField(null=True, blank=True)
    contract= models.CharField(max_length=200, null=True)
    number_of_post= models.CharField(max_length=200, null=True)
    commision=models.FloatField(null=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering =['-created']

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url

        except:
            url =""

        return url


class Countries(models.Model):
    name= models.CharField(max_length=200)
    created =models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.name



