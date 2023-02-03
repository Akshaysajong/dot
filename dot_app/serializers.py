from rest_framework import serializers
# from django.contrib.auth import get_user_model
from .models import customer,content,destinstions,destination_img,organization,organization_images,best_things,card,destination_area
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


class bannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=content
        fields = '__all__'

class destinationsSerializer(serializers.ModelSerializer):
    class Meta:
        model=destinstions
        fields = ['id','destn_type']

class destination_imgSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=destination_img
        fields = ['id','destinstions_id','image']

class placesSerializer(serializers.ModelSerializer):
    class Meta:
        model=destination_area
        fields = ['id','name','image']

# class places_imgSerializer(serializers.HyperlinkedModelSerializer):
#     id = serializers.ReadOnlyField()
#     class Meta:
#         model=destination_area
#         fields = ['id','image']
class cardSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=card
        fields = ['id','title','img']


class staysSerializer(serializers.ModelSerializer):
    class Meta:
        model=organization
        fields = ['id','title']

class staysimgSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=organization_images
        fields = ['id','images']

class bestthingsSerializer(serializers.ModelSerializer):
    class Meta:
        model=best_things
        fields = ['id','title','img']

class destinationsearchSerializer(serializers.ModelSerializer):
    class Meta:
        model=destinstions
        fields = ['id','name'],

# dot_destination_detailsAPI
class destinationdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=destination_area
        fields = ['id','place','description']

class destinationdetails_imgSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=destination_img
        fields = ['id','destinstions_id','image']

class destination_humpidetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=destinstions
        fields = ['id','name']

class destination_humpidetails_imgSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=destination_img
        fields = ['id','destinstions_id','image']

class destination_humpidescription_Serializer(serializers.ModelSerializer):
    class Meta:
        model=destinstions
        fields = ['id','description']    
# humpi_surrounding
class humpi_surroundingsSerializer(serializers.ModelSerializer):
    class Meta:
        model=destinstions
        fields = ['id','name','description']

class humpi_surroundings_imgSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=destination_img
        fields = ['id','destinstions_id','image']
        
class stay_humpiSearializer(serializers.ModelSerializer):
    class Meta:
        model=organization
        fields = ['id','title']

class stay_humpi_imgSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=organization_images
        fields = ['id','images']

