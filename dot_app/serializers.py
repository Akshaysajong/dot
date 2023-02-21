from rest_framework import serializers
# from django.contrib.auth import get_user_model
from .models import customer,content,destinstions,destination_img,content_images,organization,organization_images,best_things,card,destination_area,feedback,icons,booking,destination_type,Subscription
from rest_framework.response import Response

# register customers

class customerRegister(serializers.ModelSerializer):
    # password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=customer
        fields='__all__'

    def save(self):
        pwd=self.validated_data['pwd']
        # password2=self.validated_data['password2']
        name=self.validated_data['name'],
        print(name)
        cst= customer.objects.filter(name=self.validated_data['name']).count()
        print(cst)
        # if password != password2:
        #     raise serializers.ValidationError({'password':'password does not match'})
        if cst>0:
            raise serializers.ValidationError({'name':'User already exist'})
        else:
            reg=customer(
                    name=self.validated_data['name'],
                    email=self.validated_data['email'], 
                    pwd=self.validated_data['pwd'],                   
                    first_name=self.validated_data['first_name'],
                    last_name=self.validated_data['last_name'],
                    phone=self.validated_data['phone'],
                    cust_type=self.validated_data['cust_type'],                  
                    status=self.validated_data['status'],                                                     
            )
        reg.save()
        return reg

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
        fields = ['title','body']
        
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
        model=organization_images
        fields = ['id','images']


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
        fields = ('email', 'subscription_type', 'subscribed_date')