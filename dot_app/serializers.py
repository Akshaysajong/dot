from rest_framework import serializers
# from django.contrib.auth import get_user_model
from .models import customer,cust_profile,content,facility_image,destinstions,destination_img,content_images,organization,organization_images,best_things,card,destination_area,feedback,icons,booking,destination_type,Subscription
from rest_framework.response import Response

# register customers


class customerRegister(serializers.ModelSerializer): 
    class Meta:
        model=customer
        fields=('id','name','email','phone','gender','cust_type','status','first_name','last_name')
class CustomerProfileSerializer(serializers.ModelSerializer):
    cust = customerRegister()
    class Meta:
        model = cust_profile
        fields = ['cust','address']
    # def save(self):
    #     # pwd=self.validated_data['pwd']
    #     # password2=self.validated_data['password2']
    #     name=self.validated_data.get('name')
    #     print(name)
    #     cst= customer.objects.filter(name=self.validated_data).count()
    #     print(cst)
    #     # if password != password2:
    #     #     raise serializers.ValidationError({'password':'password does not match'})
    #     # if cst>0:
    #     #     raise serializers.ValidationError({'name':'User already exist'})
    #     # else:
    #     reg=customer(
    #             name=self.validated_data['name'],
    #             email=self.validated_data['email'], 
    #             pwd=self.validated_data['pwd'],                   
    #             first_name=self.validated_data['first_name'],
    #             last_name=self.validated_data['last_name'],
    #             phone=self.validated_data['phone'],
    #             cust_type=self.validated_data['cust_type'],    
    #             # address=self.validated_data['address'],               
    #             status=self.validated_data['status'],                                                     
    #     )
    #     reg.save()
    #     profile = cust_profile(
    #         cust_id = reg.id, 
    #         phone=self.validated_data['phone'],
    #         email=self.validated_data['email'], 
    #         address=self.validated_data['address'],
             
               
    #         status=self.validated_data['status'], 
        
    #     )
    #     profile.save()

    #     return (reg)
    



# # register customers
# class cust_profileRegister(serializers.ModelSerializer):   
#     class Meta:
#         model=cust_profile
#         fields='__all__'
#     def save(self):
#             prof=cust_profile(
#                     city=self.validated_data['city'],
#                     state=self.validated_data['state'],                    
#                     address=self.validated_data['address'],                                    
#                     status=self.validated_data['status'],
#             )
#             prof.save()
#             return prof

# destination_area
# class destination_areaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=destination_area
#         fields = '__all__'

# # view destinations
# class destinstionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=destinstions
#         fields = '__all__'

# # destination_img
# class destination_imgSerializer(serializers.HyperlinkedModelSerializer):
#     id = serializers.ReadOnlyField()
#     class Meta:
#         model=destination_img
#         fields=['id','destinstions_id','image']


# homepage
class bannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=content
        fields = ['title','path','body']
class headSerializer(serializers.ModelSerializer):
    class Meta:
        model=content
        fields = ['title','body']

class destinationsSerializer(serializers.ModelSerializer):
    class Meta:
        model=destination_type
        fields = ['id','name']

class destination_imgSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=destination_img
        fields = ['id','destinstions_id','image']

class placesSerializer(serializers.ModelSerializer):
    class Meta:
        model=destination_area
        fields = ['id','name','image']

class cardSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=content_images
        fields = ['id','image','overlay']

class staysSerializer(serializers.ModelSerializer):
    class Meta:
        model=organization
        fields = ['id','title']

class staysimgSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=organization_images
        fields = ['id','organization_id','images']

class bestthingsSerializer(serializers.ModelSerializer):
    class Meta:
        model=content_images
        fields = ['id','image','overlay']


# search autocomplete

class destinationsearchSerializer(serializers.ModelSerializer):   
    
    # destinstions =destinationimageSerializer()
    class Meta:
        model=destinstions
        fields = [ 'id','name','description']

class destinationimageSerializer(serializers.ModelSerializer):
    destinstions = destinationsearchSerializer()
    class Meta:
        model = destination_img
        fields = [ 'destinstions', 'image']


# dot_button_detailsAPI
class head_KSerializer(serializers.ModelSerializer):
    class Meta:
        model=content
        fields = ['title']
        
class buttondetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=destination_area
        fields = ['id','place','description','image']
        
class iconSerializer(serializers.ModelSerializer):
    class Meta:
        model=icons
        fields = ['id','title','img']

# destination details
class destinationdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=destinstions
        fields = ['id','name','description']

class destinationdetails_imgSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=destination_img
        fields = ['id','destinstions_id','image']
# hampi
class destination_humpidetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=destinstions
        fields = ['id','name']

class destination_humpidetails_imgSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=destination_img
        fields = ['id','destinstions_id','image']



class contentSerializer(serializers.ModelSerializer):
    class Meta:
        model = content
        fields = '__all__'

class content_imgSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = content_images
        fields = '__all__' 







class destination_humpidescription_Serializer(serializers.ModelSerializer):
    class Meta:
        model=destinstions
        fields = ['id','description']  

# hampi_surrounding
class humpi_surroundingsSerializer(serializers.ModelSerializer):
    class Meta:
        model=destinstions
        fields = ['id','name','description']

class humpi_surroundings_imgSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=destination_img
        fields = ['id','destinstions_id','image']
# stay
class stay_humpiSearializer(serializers.ModelSerializer):
    class Meta:
        model=organization
        fields = ['id','title']

class stay_humpi_imgSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=organization_images
        fields = ['id','organization_id','images']
        
class stay_feedbackSearializer(serializers.ModelSerializer):
    class Meta:
        model=feedback
        fields = ['id','name','created','feedback']

# wanderlust_hampiSerializer
class wanderlust_hampiSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=facility_image
        fields = ['id','image']


# discover more stays
class more_staysSerializer(serializers.ModelSerializer):
    class Meta:
        model=organization
        fields = ['id','title']

class more_staysimgSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=organization_images
        fields = ['id','organization_id','images']

# booking
class wanderlust_booking_Serializer(serializers.ModelSerializer):
   
    class Meta:
        model=organization
        fields = ['id','title']
class wanderlust_booking_imgSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=organization_images
        fields = ['id','images']
class roomicon_Searializer(serializers.ModelSerializer):
    class Meta:
        model=icons
        fields = ['id','title','img']
class room_bookingSearializer(serializers.ModelSerializer):
    class Meta:
        model=booking
        fields = ['id','bk_from','bk_to','guests']
# category search
class categorysearchSerializer(serializers.ModelSerializer):
    class Meta:
        model=icons
        fields = ['id','title','img']




# from autocomplete_light.serializers import AutocompleteSerializer

class MyModelSerializer(destinationsearchSerializer):
    class Meta:
        model = destinstions
        fields = ['name'] 


# subscription
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('email', 'subscribed_date')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = destinstions
        fields = ['name','address','description']
class Location_imgSerializer(serializers.ModelSerializer):
    class Meta:
        model = destination_img
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = destinstions
        fields = ['name','address','description']

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = destinstions
        fields = ['bk_from','bk_to','cust_id']


# book hotel
class hotel_bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields =  ['cust','bk_from','bk_to','title','guests','status']


from .models import customer

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ['id', 'name', 'email', 'phone','gender']
        extra_kwargs = {'password': {'write_only': True}}


# from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
# from django.core.validators import validate_email
# from phonenumbers import parse, is_valid_number

# class EditAccountSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         required=True,
#         validators=[UniqueValidator(queryset=customer.objects.all())]
#     )
#     phone_number = serializers.CharField(
#         required=True,
#         max_length=17
#     )

#     def validate_email(self, value):
#         try:
#             validate_email(value)
#         except:
#             raise serializers.ValidationError("Invalid email address")
#         return value

#     def validate_phone_number(self, value):
#         try:
#             parsed_number = parse(value, None)
#             if not is_valid_number(parsed_number):
#                 raise serializers.ValidationError("Invalid phone number")
#         except:
#             raise serializers.ValidationError("Invalid phone number")
#         return value

#     class Meta:
#         model = customer
#         fields = ('email', 'phone')

from rest_framework.exceptions import ValidationError
# import re

# from django.core.validators import EmailValidator, RegexValidator

from django.core.validators import validate_email
from rest_framework import serializers

class edit_customerSerializer(serializers.ModelSerializer):

    # email = serializers.CharField(validators=[validate_email])
    # phone = serializers.CharField(max_length=10, min_length=10)

    class Meta:
        model = customer
        fields = ['id', 'name', 'email', 'phone','gender']
    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError(' enter a valid email address')
        return value

    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError('Phone number should contain only digits')
        if len(value) != 10:            
            raise serializers.ValidationError('Phone number should be 10 digits long')
        return value



    # class Meta:
    #     model = customer
    #     fields =  ['name', 'email', 'phone','gender']


# class edit_customerSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(validators=[EmailValidator()])
    # phone = serializers.CharField(validators=[RegexValidator(r'^\+?[1-9]\d{1,14}$')])

    # class Meta:
    #     model = customer
    #     fields = ['name','first_name', 'last_name', 'email', 'phone','gender']

        
    # def update(self, instance, validated_data):
       
        # email = validated_data.get('email', instance.email)
        # if not email or not validate_email(email):
        #     raise ValidationError({'email': 'Invalid email'})


        # phone = validated_data.get('phone', instance.phone)
        # if not phone or not validate_phone(phone):
        #     raise ValidationError({'phone': 'Invalid phone number'})
        

    # def validate(self, attrs):
    #     email = attrs.get('email')
    #     phone = attrs.get('phone')
        
    #     if email and customer.objects.exclude(name=self.instance.name).filter(email=email).exists():
    #         raise serializers.ValidationError('Email already in use.')
        
    #     if phone and customer.objects.exclude(name=self.instance.name).filter(phone=phone).exists():
    #         raise serializers.ValidationError('Phone number already in use.')
        
    #     return attrs

# from django.core.validators import validate_email
# from django.core.exceptions import ValidationError
# import phonenumbers
# def validate_email_address(email):
#     try:
#         validate_email(email)
#         return True
#     except ValidationError:
#         return False


# def validate_phone_number(phone_number, country_code):
#     try:
#         parsed_phone_number = phonenumbers.parse(phone_number, country_code)
#         return phonenumbers.is_valid_number(parsed_phone_number)
#     except phonenumbers.phonenumberutil.NumberParseException:
#         return False

#     # def update(self, instance, validated_data):
       
    #     email = validated_data.get('email', instance.email)
    #     if not email or not validate_email(email):
    #         raise ValidationError({'email': 'Invalid email'})


    #     phone = validated_data.get('phone', instance.phone)
    #     if not phone or not validate_phone(phone):
    #         raise ValidationError({'phone': 'Invalid phone number'})

       
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.email = email
    #     instance.phone = phone
    #     # instance.address = validated_data.get('address', instance.address)
    #     instance.save()
    #     return instance

    # def validate_email(email):
    #     if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
    #         raise ValidationError('Invalid email format')
    #     return email

#     def validate_phone(phone):
#         if not re.match(r'^\+?\d{10,14}$', phone):
#             raise ValidationError('Invalid phone number format')
#         return phone


from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework import serializers

from .models import customer,memories_img,memories


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ('id', 'name', 'email', 'phone')

    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError('Please enter a valid email address')
        return value

    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError('Phone number should contain only digits')
        if len(value) != 10:            
            raise serializers.ValidationError('Phone number should be 10 digits long')
        return value



from .models import facility_Review,destination_Review,organization_Review

class organizationReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = organization_Review
        fields =  '__all__'
class facilityReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = facility_Review
        fields =  '__all__'

class destinationReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = destination_Review
        fields = '__all__'

# add memory
# class memoryImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = memories_img
#         fields = ('id', 'image')

# class MemorySerializer(serializers.ModelSerializer):
#     images = memoryImageSerializer()
#     class Meta:
#         model = memories      
#         fields = ('id', 'cust_id','destinstion','created','updated','destn_facility', 'experience', 'memories','visited_date', 'images','status')
  
class MemorySerializer(serializers.ModelSerializer): 
    class Meta:
        model=memories
        fields=('id', 'cust_id','destinstion','created','updated','destn_facility', 'experience', 'memories','visited_date','status')
class memoryImageSerializer(serializers.ModelSerializer):
    memories = MemorySerializer()
    class Meta:
        model = memories_img
        fields =['id', 'image','memories']
    # def mem(self, validated_data):
       
    #     return mem
    
# travel memory
class travelMemoryimgSerializer(serializers.ModelSerializer):
    class Meta:
        model = memories_img
        fields = ('memories_id', 'image')

class travelMemorySerializer(serializers.ModelSerializer):
    image = travelMemoryimgSerializer(many=True, read_only=True)
    class Meta:
        model = memories      
        fields = ('id', 'cust_id','destinstion','created','updated','organzn', 'experience', 'memories','visited_date', 'image','status')
# memory details
from .models import memories,destn_facility
class memorydetailsImageSerializer(serializers.ModelSerializer):
     class Meta:
        model = memories_img
        fields = ['image']
class MemorydetailsSerializer(serializers.ModelSerializer):
    images = memoryImageSerializer(many=True, read_only=True)
    class Meta:
        model = memories      
        fields = ('id', 'cust_id','destinstion','created','updated','destn_facility', 'experience', 'memories','visited_date', 'images','status')

class wanderlust_reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = facility_Review
        fields = ('id','cust_id','created','review')


class facilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = destn_facility
        fields = ('orgatn','description','amount')
# book hotel
from rest_framework import serializers

class HotelSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    address = serializers.CharField()
  

class HotelImageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    organization_id = serializers.IntegerField()
    image_url = serializers.CharField()

class RoomSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    hotel_id = serializers.IntegerField()
    name = serializers.CharField()

class RoomPriceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    room_id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

class RoomImageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    room_id = serializers.IntegerField()
    image_url = serializers.CharField()


# from rest_framework import serializers
# from .models import Hotel, HotelImage, Room, RoomImage, RoomPrice

# class HotelImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HotelImage
#         fields = ('image',)

# class RoomImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RoomImage
#         fields = ('image',)

# class RoomPriceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RoomPrice
#         fields = ('date', 'price')

# class RoomSerializer(serializers.ModelSerializer):
#     images = RoomImageSerializer(many=True)
#     prices = RoomPriceSerializer(many=True)

#     class Meta:
#         model = Room
#         fields = ('id', 'room_type', 'description', 'max_guests', 'images', 'prices')

# class HotelSerializer(serializers.ModelSerializer):
#     images = HotelImageSerializer(many=True)
#     rooms = RoomSerializer(many=True)

#     class Meta:
#         model = Hotel
#         fields = ('id', 'name', 'address', 'city', 'state', 'country', 'images', 'rooms')

# class HotelBookingSerializer(serializers.Serializer):
#     hotel_id = serializers.IntegerField()
#     room_id = serializers.IntegerField()
#     check_in = serializers.DateField()
#     check_out = serializers.DateField()
#     num_guests = serializers.IntegerField()

#     def validate(self, data):
#         # Check if hotel and room exist
#         hotel = Hotel.objects.filter(id=data['hotel_id']).first()
#         if not hotel:
#             raise serializers.ValidationError('Invalid hotel id')
#         room = Room.objects.filter(id=data['room_id']).first()
#         if not room:
#             raise serializers.ValidationError('Invalid room id')

#         # Check if dates are valid
#         if data['check_in'] >= data['check_out']:
#             raise serializers.ValidationError('Check-in date must be before check-out date')

#         # Check if number of guests does not exceed max guests for the room
#         if data['num_guests'] > room.max_guests:
#             raise serializers.ValidationError('Number of guests exceeds room capacity')

#         # Check if there is availability for the room in the specified dates
#         prices = room.prices.filter(date__range=(data['check_in'], data['check_out'])).values_list('price', flat=True)
#         if len(prices) == 0:
#             raise serializers.ValidationError('No availability for the room in the specified dates')
#         total_price = sum(prices) * (data['check
