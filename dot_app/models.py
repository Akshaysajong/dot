from django.db import models
from django.contrib.auth.models import AbstractUser, User

class destination_area(models.Model):
    name = models.CharField(max_length=200, default=None, blank=True)
    place = models.CharField(max_length=100, default=None, blank=True)
    lattitude = models.DecimalField(max_digits=8, decimal_places=3, default=None, blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=3, default=None, blank=True)
    status = models.BooleanField()

class destination_type(models.Model):
    name = models.CharField(max_length=50, blank=True, default=None)
    description = models.CharField(max_length=200, default=None, blank=True)
    status = models.BooleanField(default=False)

class destinstions(models.Model):
    name = models.CharField(max_length=100, default=None, blank=True)
    d_area = models.ForeignKey(destination_area, default=None, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, default=None, blank=True)
    description = models.TextField()
    climate = models.TextField()
    culture = models.TextField()
    lattitude = models.DecimalField(max_digits=8, decimal_places=3, default=None, blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=3, default=None, blank=True)
    status = models.BooleanField(default=False)

class destination_img(models.Model):
    destinstions = models.ForeignKey(destinstions, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/', blank=True)

class destn_geography(models.Model):
    destinstions = models.ForeignKey(destinstions, default=None, on_delete=models.CASCADE)
    types = models.CharField(max_length=100, default=None, blank=True)
    title = models.CharField(max_length=100, default=None, blank=True)
    description = models.CharField(max_length=200, default=None, blank=True)
    status = models.BooleanField(default=False)

class destn_facility(models.Model):
    destinstions = models.ForeignKey(destinstions, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default=None, blank=True)
    description = models.CharField(max_length=200, default=None, blank=True)
    types = models.CharField(max_length=100, default=None, blank=True)
    lattitude = models.DecimalField(max_digits=8, decimal_places=3, default=None, blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=3, default=None, blank=True)
    status = models.BooleanField(default=False)

class facility_price(models.Model):
    dstn_facility = models.ForeignKey(destinstions, default=None, on_delete=models.CASCADE)
    amount = models.FloatField(default=None, blank=True)
    discount = models.FloatField(default=None, blank=True)
    total = models.FloatField(default=None, blank=True)
    status = models.BooleanField(default=False)

class facility_image(models.Model):
    destinstion = models.ForeignKey(destinstions, default=None, on_delete=models.CASCADE)  
    facility = models.ForeignKey(destn_facility, default=None, on_delete=models.CASCADE) 
    imagetype = models.CharField(max_length=200, default=None, blank=True)
    image = models.ImageField(upload_to = 'images/', blank=True)
    status = models.BooleanField(default=False)

class country(models.Model):
    name = models.CharField(max_length=200, default=None, blank=True)
    location = models.CharField(max_length=200, default=None, blank=True)
    lattitude = models.DecimalField(max_digits=8, decimal_places=3, default=None, blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=3, default=None, blank=True)
    status = models.BooleanField(default=False)

class state(models.Model):
    name = models.CharField(max_length=200, default=None, blank=True)
    location = models.CharField(max_length=200, default=None, blank=True)
    lattitude = models.DecimalField(max_digits=8, decimal_places=3, default=None, blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=3, default=None, blank=True)
    country_id = models.ForeignKey(country, default=None, on_delete=models.CASCADE)  
    status = models.BooleanField(default=False)

class city(models.Model):
    name = models.CharField(max_length=200, default=None, blank=True)
    location = models.CharField(max_length=200, default=None, blank=True)
    lattitude = models.DecimalField(max_digits=8, decimal_places=3, default=None, blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=3, default=None, blank=True)
    state_id = models.ForeignKey(state, default=None, on_delete=models.CASCADE)  
    status = models.BooleanField(default=False)

class organization(models.Model):
    title = models.CharField(max_length=200,blank=True, null=True)
    org_type = models.CharField(max_length=200,blank=True, null=True)
    destinstion = models.ForeignKey(destinstions, default=None, on_delete=models.CASCADE)  
    facility = models.ForeignKey(destn_facility, default=None, on_delete=models.CASCADE) 
    contact_person = models.CharField(max_length=200,blank=True, null=True)
    contact_number = models.CharField(max_length=200,blank=True, null=True)
    website = models.CharField(max_length=200,blank=True, null=True)
    city = models.CharField(max_length=200,blank=True, null=True)
    state = models.CharField(max_length=200,blank=True, null=True)
    address = models.CharField(max_length=200,blank=True, null=True)
    phone = models.CharField(max_length=200,blank=True, null=True)
    email = models.EmailField(max_length=200,blank=True, null=True)
    proof = models.CharField(max_length=200,blank=True, null=True)
    status = models.BooleanField(default=False)

class organization_images(models.Model):
    organization = models.ForeignKey(organization, default=None, on_delete=models.CASCADE) 
    images = models.ImageField(upload_to = 'images/', blank=True)

class userprofile(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200,blank=True, null=True)
    address = models.CharField(max_length=200,blank=True, null=True)
    organization = models.ForeignKey(organization, default=None, on_delete=models.CASCADE) 
    city = models.CharField(max_length=200,blank=True, null=True)
    state = models.CharField(max_length=200,blank=True, null=True)
    address = models.CharField(max_length=200,blank=True, null=True)
    phone = models.CharField(max_length=200,blank=True, null=True)
    email = models.EmailField(max_length=200,blank=True, null=True)
    status = models.BooleanField(default=False)


    
class content(models.Model):
    content_type = models.CharField(max_length=200,blank=True, null=True)
    title = models.CharField(max_length=200,blank=True, null=True)
    page = models.CharField(max_length=200,blank=True, null=True)
    path = models.FilePathField(path=None, match=None, recursive=False, max_length=100)
    body = models.CharField(max_length=200,blank=True, null=True)
    created = models.DateTimeField(max_length=200,blank=True, null=True)
    updated = models.DateTimeField(max_length=200,blank=True, null=True)
    status = models.BooleanField(default=False)

class content_images(models.Model):
    cid = models.ForeignKey(content, default=None, on_delete=models.CASCADE) 
    content = models.CharField(max_length=200,blank=True, null=True)
    image = models.ImageField(upload_to = 'images/', blank=True)
    overlay = models.CharField(max_length=200,blank=True, null=True)
    weight = models.IntegerField(max_length=200,blank=True, null=True)
    created = models.DateTimeField(max_length=200,blank=True, null=True)
    status =  models.BooleanField(default=False)

class faq_category(models.Model):
    name = models.CharField(max_length=200,blank=True, null=True)
    description = models.CharField(max_length=200,blank=True, null=True)
    popularity = models.CharField(max_length=200,blank=True, null=True)
    status =  models.BooleanField(default=False)

class faq(models.Model):
    title = models.CharField(max_length=200,blank=True, null=True)
    description = models.CharField(max_length=200,blank=True, null=True)
    category = models.CharField(max_length=200,blank=True, null=True)
    access = models.CharField(max_length=200,blank=True, null=True)
    access_count = models.CharField(max_length=200,blank=True, null=True)
    likes = models.CharField(max_length=200,blank=True, null=True)
    dislike = models.CharField(max_length=200,blank=True, null=True)
    status = models.BooleanField(default=False)


