from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True,blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    username=models.CharField(max_length=200, null=True,blank=True)
    phone= models.CharField(max_length=200, null=True,blank=True)
    company_registartion_certificate= models.FileField(upload_to="agency_uploads",null=True, blank=True)
    nea_certificate=models.FileField(upload_to="agency_uploads",null=True, blank=True)
    cr12=models.FileField(upload_to="agency_uploads",null=True, blank=True)
    chamber_of_commerce_certificate=models.FileField(upload_to="agency_uploads",null=True, blank=True)
    union_certificate=models.FileField(upload_to="agency_uploads",null=True, blank=True)
    physical_address=models.CharField(max_length=255,null=True, blank=True)
    number_of_years_operations=models.IntegerField(null=True, blank=True)
    profile_image= models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/user-default.png')
    social_linkedin=models.CharField(max_length=200, null=True,blank=True)
    social_twitter=models.CharField(max_length=200, null=True,blank=True)
    social_youtube=models.CharField(max_length=200, null=True,blank=True)
    social_website=models.CharField(max_length=200, null=True,blank=True)
    created =models.DateTimeField(auto_now_add=True)
    has_applied= models.BooleanField(default=False)
    is_approved= models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    about_agency=models.TextField(null=True, blank=True)
    id= models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)
    is_suspended= models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering =['-created']

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url

        except:
            url =""

        return url
    @property
    def chamberCommerce(self):
        try:
            url = self.chamber_of_commerce_certificate.url

        except:
            url =""

        return url
    @property
    def companyRegistartionCert(self):
        try:
            url = self.company_registartion_certificate.url

        except:
            url =""

        return url
    @property
    def neaCert(self):
        try:
            url = self.nea_certificate.url

        except:
            url =""

        return url
    @property
    def c12(self):
        try:
            url = self.c12.url

        except:
            url =""

        return url

class Message(models.Model):
    EDUCTATION ={
        ('Primary School', 'Primary School'),
        ('High School', 'High School'),
        ('College', 'College'),
        ('University', 'University'),

    }
    COUNTIES={
        ('Nairobi','Nairobi'),
        ('Mombasa','Mombasa'),
        ("Muranga","Muranga"),
        ('Kwale','Kwale'),
        ('Kilifi','Kilifi'),
        ('Tana River','Tana River'),
        ('Lamu','Lamu'),
        ('Taita–Taveta','Taita–Taveta'),
        ('Garissa','Garissa'),
        ('Wajir','Wajir'),
        ('Mandera','Mandera'),
        ('Marsabit','Marsabit'),
        ('Isiolo','Isiolo'),
        ('Meru','Meru'),
        ('Tharaka-Nithi','Tharaka-Nithi'),
        ('Embu','Embu'),
        ('Kitui','Kitui'),
        ('Machakos','Machakos'),
        ('Makueni','Makueni'),
        ('Nyandarua','Nyandarua'),
        ('Nyeri','Nyeri'),
        ('Kirinyaga','Kirinyaga'),
        ('Kiambu','Kiambu'),
        ('Turkana','Turkana'),
        ('West Pokot','West Pokot'),
        ('Samburu','Samburu'),
        ('Trans-Nzoia','Trans-Nzoia'),
        ('Uasin Gishu','Uasin Gishu'),
        ('Elgeyo-Marakwet','Elgeyo-Marakwet'),
        ('Nandi','Nandi'),
        ('Baringo','Baringo'),
        ('Laikipia','Laikipia'),
        ('Nakuru','Nakuru'),
        ('Narok','Narok'),
        ('Kajiado','Kajiado'),
        ('Kericho','Kericho'),
        ('Bomet','Bomet'),
        ('Kakamega','Kakamega'),
        ('Vihiga','Vihiga'),
        ('Bungoma','Bungoma'),
        ('Busia','Busia'),
        ('Siaya','Siaya'),
        ('Kisumu','Kisumu'),
        ('Homa Bay','Homa Bay'),
        ('Migori','Migori'),
        ('Kisii','Kisii'),
        ('Nyamira','Nyamira'),
    }
    VALID_PASSPORT={
        ('YES','YES'),
        ('NO','NO'),
    }
    VALID_GOOD={
        ('YES','YES'),
        ('NO','NO'),
    }
    sender= models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='messages')
    name= models.CharField(max_length=200, null=True, blank=True)
    phone= models.CharField(max_length=200, null=True, blank=True)
    email= models.EmailField(max_length=200, null=True, blank=True)
    subject= models.CharField(max_length=200, null=True, blank=True)
    age=models.IntegerField(null=True, blank=True)
    education_level=models.CharField(max_length=200, choices=EDUCTATION, null=True, blank=True )
    body= models.TextField()
    valid_passport=models.CharField(max_length=200,choices=VALID_PASSPORT, default="NO")
    valid_good_conduct=models.CharField(max_length=200,choices=VALID_GOOD, default="NO")
    county=models.CharField(max_length=200, choices=COUNTIES, null=True, blank=True )

    is_read = models.BooleanField(default=False, null=True)
    created =models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.subject)

    class Meta:
        ordering=['is_read', '-created']


class Application(models.Model):
    EDUCTATION ={
        ('Primary School', 'Primary School'),
        ('High School', 'High School'),
        ('College', 'College'),
        ('University', 'University'),

    }
    COUNTIES={
        ('Nairobi','Nairobi'),
        ('Mombasa','Mombasa'),
        ("Muranga","Muranga"),
        ('Kwale','Kwale'),
        ('Kilifi','Kilifi'),
        ('Tana River','Tana River'),
        ('Lamu','Lamu'),
        ('Taita–Taveta','Taita–Taveta'),
        ('Garissa','Garissa'),
        ('Wajir','Wajir'),
        ('Mandera','Mandera'),
        ('Marsabit','Marsabit'),
        ('Isiolo','Isiolo'),
        ('Meru','Meru'),
        ('Tharaka-Nithi','Tharaka-Nithi'),
        ('Embu','Embu'),
        ('Kitui','Kitui'),
        ('Machakos','Machakos'),
        ('Makueni','Makueni'),
        ('Nyandarua','Nyandarua'),
        ('Nyeri','Nyeri'),
        ('Kirinyaga','Kirinyaga'),
        ('Kiambu','Kiambu'),
        ('Turkana','Turkana'),
        ('West Pokot','West Pokot'),
        ('Samburu','Samburu'),
        ('Trans-Nzoia','Trans-Nzoia'),
        ('Uasin Gishu','Uasin Gishu'),
        ('Elgeyo-Marakwet','Elgeyo-Marakwet'),
        ('Nandi','Nandi'),
        ('Baringo','Baringo'),
        ('Laikipia','Laikipia'),
        ('Nakuru','Nakuru'),
        ('Narok','Narok'),
        ('Kajiado','Kajiado'),
        ('Kericho','Kericho'),
        ('Bomet','Bomet'),
        ('Kakamega','Kakamega'),
        ('Vihiga','Vihiga'),
        ('Bungoma','Bungoma'),
        ('Busia','Busia'),
        ('Siaya','Siaya'),
        ('Kisumu','Kisumu'),
        ('Homa Bay','Homa Bay'),
        ('Migori','Migori'),
        ('Kisii','Kisii'),
        ('Nyamira','Nyamira'),
    }
    VALID_PASSPORT={
        ('YES','YES'),
        ('NO','NO'),
    }
    VALID_GOOD={
        ('YES','YES'),
        ('NO','NO'),
    }
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='application')
    name= models.CharField(max_length=200, null=True, blank=True)
    phone= models.CharField(max_length=200, null=True, blank=True)
    email= models.EmailField(max_length=200, null=True, blank=True)
    age=models.IntegerField(null=True, blank=True)
    education_level=models.CharField(max_length=200, choices=EDUCTATION, null=True, blank=True )
    valid_passport=models.CharField(max_length=200,choices=VALID_PASSPORT, default="NO")
    valid_good_conduct=models.CharField(max_length=200,choices=VALID_GOOD, default="NO")
    county=models.CharField(max_length=200, choices=COUNTIES, null=True, blank=True )
    is_read = models.BooleanField(default=False, null=True)
    created =models.DateTimeField(auto_now_add=True)
    job_title=models.CharField(max_length=200, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.job_title)

    class Meta:
        ordering=['is_read', '-created']



