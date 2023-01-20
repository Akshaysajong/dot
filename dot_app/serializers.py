from rest_framework import serializers
# from django.contrib.auth import get_user_model
from .models import customer
from rest_framework.response import Response
# register customers
class customerRegister(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=customer
        fields='__all__'
    def save(self):
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        username=self.validated_data['username'],
        print(username)
        cst= customer.objects.filter(username=self.validated_data['username']).count()
        print(cst)
        if password != password2:
            raise serializers.ValidationError({'password':'password does not match'})
        elif cst>0:
            raise serializers.ValidationError({'username':'User already exist'})
        else:
            reg=customer(
                    username=self.validated_data['username'],
                    email=self.validated_data['email'],                    
                    first_name=self.validated_data['first_name'],
                    last_name=self.validated_data['last_name'],
                    phone=self.validated_data['phone'],
                    cust_type=self.validated_data['cust_type'],                  
                    status=self.validated_data['status'],
            )
        reg.save()
        return reg