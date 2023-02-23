from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.hashers import make_password
from django_filters import FilterSet


class destarea_type(models.Model):
    name = models.CharField(max_length=200, default=None, blank=True)

class destination_area(models.Model):
    name = models.CharField(max_length=200, default=None, blank=True)
    place = models.CharField(max_length=100, default=None, blank=True)
    description = models.TextField(max_length=200, default=None, blank=True)    
    image = models.ImageField(upload_to = 'images/', blank=True)
    country = models.CharField(max_length=100, default=None, blank=True)
    state = models.CharField(max_length=100, default=None, blank=True) 
    lattitude = models.DecimalField(max_digits=8, decimal_places=3, default=None, blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=3, default=None, blank=True)
    status = models.BooleanField()
    c_user = models.CharField(max_length=100, default=None, blank=True)

class destinationarea_type(models.Model):
    destnarea_type = models.ForeignKey(destarea_type, default=None, on_delete=models.CASCADE)
    destnarea = models.ForeignKey(destination_area, default=None, on_delete=models.CASCADE)

class destination_type(models.Model):
    name = models.CharField(max_length=50, blank=True, default=None)
    description = models.CharField(max_length=200, default=None, blank=True)
    status = models.BooleanField(default=False)

class destinstions(models.Model):
    name = models.CharField(max_length=100, default=None, blank=True)
    d_area = models.ForeignKey(destination_area, default=None, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, default=None, blank=True)
    description = models.TextField(max_length=200, default=None, blank=True)    
    culture = models.TextField(max_length=200, default=None, blank=True)
    climate = models.TextField(max_length=200, default=None, blank=True)
    lattitude = models.DecimalField(max_digits=8, decimal_places=3, default=None, blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=3, default=None, blank=True)
    status = models.BooleanField(default=False)
    c_user = models.CharField(max_length=100, default=None, blank=True)
    destn_type = models.CharField(max_length=100, default=None, blank=True)

class destination_img(models.Model):
    destinstions = models.ForeignKey(destinstions, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/', blank=True)

class destn_geography(models.Model):
    destinstions = models.ForeignKey(destinstions, default=None, on_delete=models.CASCADE)
    types = models.CharField(max_length=100, default=None, blank=True)
    title = models.CharField(max_length=100, default=None, blank=True)
    description = models.CharField(max_length=200, default=None, blank=True)
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

class hotel_type(models.Model):
    types = models.CharField(max_length=200, default=None, blank=True)
    
class organization(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,blank=True, null=True)
    org_type = models.CharField(max_length=200,blank=True, null=True)
    destinstion = models.ForeignKey(destinstions, default=None, on_delete=models.CASCADE)  
    contact_person = models.CharField(max_length=200,blank=True, null=True)
    contact_number = models.CharField(max_length=200,blank=True, null=True)
    website = models.CharField(max_length=200,blank=True, null=True)
    city = models.ForeignKey(city, default=None, on_delete=models.CASCADE) 
    state = models.ForeignKey(state, default=None, on_delete=models.CASCADE) 
    address = models.CharField(max_length=200,blank=True, null=True)
    phone = models.CharField(max_length=200,blank=True, null=True)
    email = models.EmailField(max_length=200,blank=True, null=True)
    proof = models.CharField(max_length=200,blank=True, null=True)
    status = models.BooleanField(default=True)
    c_user = models.CharField(max_length=100, default=None, blank=True)

class facility_type(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    status = models.BooleanField(default=False)

class destn_facility(models.Model):
    destinstions = models.CharField(max_length=100, default=None, blank=True)
    orgatn = models.CharField(max_length=100, default=None, blank=True)
    title = models.CharField(max_length=100, default=None, blank=True)
    description = models.CharField(max_length=200, default=None, blank=True)
    types = models.CharField(max_length=100, default=None, blank=True)
    amount = models.FloatField(default=None, blank=True)
    status = models.BooleanField(default=False)
    c_user = models.CharField(max_length=100, default=None, blank=True)

class facility_price(models.Model):
    dstn_facility = models.ForeignKey(destinstions, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default=None, blank=True)
    amount = models.FloatField(default=None, blank=True)
    discount = models.FloatField(default=None, blank=True)
    total = models.FloatField(default=None, blank=True)
    status = models.BooleanField(default=False)

class facility_image(models.Model):
    destinstion =  models.CharField(max_length=100, default=None, blank=True)
    facility = models.ForeignKey(destn_facility, default=None, on_delete=models.CASCADE) 
    imagetype = models.CharField(max_length=200, default=None, blank=True)
    image = models.ImageField(upload_to = 'images/', blank=True)
    status = models.BooleanField(default=False)
    c_user = models.CharField(max_length=100, default=None, blank=True)

class organization_images(models.Model):
    organization = models.ForeignKey(organization, default=None, on_delete=models.CASCADE) 
    images = models.ImageField(upload_to = 'images/', blank=True)

class userprofile(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default=None, blank=True)
    phone = models.CharField(max_length=200,blank=True, null=True)
    address = models.CharField(max_length=200,blank=True, null=True)
    # hotel_type = models.CharField(max_length=200,blank=True, null=True)
    # contact_person = models.CharField(max_length=200,blank=True, null=True)
    # organization = models.ForeignKey(organization, default=None, on_delete=models.CASCADE) 
    # city = models.CharField(max_length=200,blank=True, null=True)
    # state = models.CharField(max_length=200,blank=True, null=True)
    # country = models.CharField(max_length=200,blank=True, null=True)
    # email = models.EmailField(max_length=200,blank=True, null=True)
    status = models.BooleanField(default=False)
    c_user = models.CharField(max_length=100, default=None, blank=True)
    
class content(models.Model):
    content_type = models.CharField(max_length=200,blank=True, null=True)
    title = models.CharField(max_length=200,blank=True, null=True)
    page = models.CharField(max_length=200,blank=True, null=True)
    path = models.CharField(max_length=200,blank=True, null=True)
    body = models.CharField(max_length=200,blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    c_user = models.CharField(max_length=200,blank=True, null=True)

class content_images(models.Model):
    cid = models.CharField(max_length=200,blank=True, null=True)
    content = models.CharField(max_length=200,blank=True, null=True)
    image = models.ImageField(upload_to = 'images/', blank=True)
    overlay = models.CharField(max_length=200,blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    status =  models.BooleanField(default=False)
    c_user = models.CharField(max_length=200,blank=True, null=True)

class faq_category(models.Model):
    name = models.CharField(max_length=200,blank=True, null=True)
    description = models.CharField(max_length=200,blank=True, null=True)
    popularity = models.CharField(max_length=200,blank=True, null=True, default='0')
    status =  models.BooleanField(default=False,blank=True, null=True,)

class faq(models.Model):
    title = models.CharField(max_length=200,blank=True, null=True)
    description = models.CharField(max_length=200,blank=True, null=True)
    category = models.CharField(max_length=200,blank=True, null=True)
    access = models.CharField(max_length=200,blank=True, null=True)
    access_count = models.CharField(max_length=200,blank=True, null=True, default='0')
    likes = models.CharField(max_length=200,blank=True, null=True, default='0')
    dislike = models.CharField(max_length=200,blank=True, null=True, default='0')
    status = models.BooleanField(default=False)

class customer_type(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
    status = models.BooleanField(default=False)

class customer(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
    pwd= models.CharField(max_length=50,blank=True, null=True)
    first_name = models.CharField(max_length=50,blank=True, null=True)
    last_name = models.CharField(max_length=50,blank=True, null=True)
    email = models.EmailField(max_length = 254)
    phone = models.CharField(max_length=50,blank=True, null=True)
    cust_type = models.CharField(max_length=50,blank=True, null=True)
    gender= models.CharField(max_length=50,blank=True, null=True)
    status = models.BooleanField(default=False)

class cust_profile(models.Model):
    cust = models.ForeignKey(customer, default=None, on_delete=models.CASCADE)
    city = models.CharField(max_length=50,blank=True, null=True)
    state = models.CharField(max_length=50,blank=True, null=True)
    address = models.CharField(max_length=50,blank=True, null=True)
    phone = models.CharField(max_length=50,blank=True, null=True)
    email = models.EmailField(max_length=200,blank=True, null=True)
    status = models.BooleanField(default=False)

class customer_auth(models.Model):
    u_id=models.ForeignKey(customer,default=None,on_delete=models.CASCADE) 
    tokens=models.CharField(max_length=100,default="")
    username=models.CharField(max_length=50,default="") 
    # def __str__(self):
    #     return self.username

class booking_type(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=200, default=None, blank=True)
    status = models.BooleanField(default=False)

class booking(models.Model):
    title = models.CharField(max_length=50,blank=True, null=True)
    bking_type = models.CharField(max_length=50,blank=True, null=True)
    bk_from = models.CharField(max_length=50,blank=True, null=True)
    bk_to = models.CharField(max_length=50,blank=True, null=True)
    cust = models.ForeignKey(customer, default=None, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    guests = models.IntegerField(max_length=50,blank=True, null=True)
    status = models.CharField(max_length=50,blank=True, null=True, default='pending')

class coupon_type(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
    label = models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=50,blank=True, null=True)
    status = models.BooleanField(default=False)

class coupon(models.Model):
    code = models.CharField(max_length=50,blank=True, null=True)
    c_type = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(max_length=50,blank=True, null=True)
    amount_type = models.CharField(max_length=50,blank=True, null=True)
    usage_limit = models.IntegerField(blank=True, null=True)
    used_by = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    expiry = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)

class feedback(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    feedback = models.CharField(max_length=500,blank=True, null=True)

class faq_category(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=200,blank=True, null=True)
    popularity = models.CharField(max_length=100,blank=True, null=True)
    status = models.BooleanField(default=False)


class staff_department(models.Model):   
    department =models.CharField(max_length=50,blank=True, null=True)
    status = models.BooleanField(default=False)

class best_things(models.Model):
    title=models.CharField(max_length=50,blank=True, null=True)
    img=models.ImageField(upload_to = 'images/', blank=True)

class card(models.Model):
    title=models.CharField(max_length=50,blank=True, null=True)
    img=models.ImageField(upload_to = 'images/', blank=True)


class icons(models.Model):
    name=models.CharField(max_length=50,blank=True, null=True)
    title=models.CharField(max_length=50,blank=True, null=True)
    img=models.ImageField(upload_to = 'images/', blank=True)



class Subscription(models.Model):
    email = models.EmailField()
    subscription_type = models.CharField(max_length=50)
    subscribed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.email



class facility_Review(models.Model):
    destn_facility_id = models.CharField(max_length=100,blank=True, null=True, default=0)
    cust_id= models.ForeignKey(customer, default=None, on_delete=models.CASCADE)
    rating=models.IntegerField(blank=True, null=True)
    review=models.CharField(max_length=100,blank=True, null=True)
    user_id = models.CharField(max_length=100,blank=True, null=True, default=0)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=100,blank=True, null=True)

class destination_Review(models.Model):
    destinstion_id = models.CharField(max_length=100,blank=True, null=True, default=0)
    cust_id = models.ForeignKey(customer, default=None, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, null=True)
    review = models.CharField(max_length=100,blank=True, null=True)
    user_id = models.CharField(max_length=100,blank=True, null=True, default=0)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=100,blank=True, null=True)

class memories(models.Model):
    cust_id = models.ForeignKey(customer, default=None, on_delete=models.CASCADE)
    destinstions = models.CharField(max_length=100,blank=True, null=True, default=0)
    destn_facility = models.CharField(max_length=100,blank=True, null=True, default=0)
    experience = models.CharField(max_length=200,blank=True, null=True)
    memories = models.CharField(max_length=200,blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    visited_date=models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=100,blank=True, null=True, default=0)
    status = models.CharField(max_length=200,blank=True, null=True)
    
class memories_img(models.Model):
    memories = models.ForeignKey(memories, on_delete=models.CASCADE)
    image=models.ImageField(upload_to = 'images/', blank=True)

    

