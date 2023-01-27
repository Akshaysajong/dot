from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import update_session_auth_hash
from .form import RegisterForm,AddHotelsForm,AddHotel_staffForm
from django.http import JsonResponse



def login_user(request):
    form = AuthenticationForm
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            if user.is_superuser:
                login(request, user) 
                messages.info(request,  {username}) 
                return redirect("dot_dashboard")
            else:
                login(request, user) 
                print("333333333333333333333333333333333333333")
                messages.info(request, {username}) 
                messages.info(request, f"You are now logged in as {id}") 
                return redirect('dot_dashboard')
        else:
            return render(request,"login.html",{'msg':'username or password is incorrect'})
    return render(request, "login.html",{'form': form})

@login_required(login_url="/login")
def dot_dashboard(request):
    return render(request, 'dashboard.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required(login_url="/login")
def dot_adduser(request):
    form = RegisterForm
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            print(username)
            gr_id = request.POST.getlist('groups')
            idd= gr_id[0]
            print(gr_id)
            for x in  gr_id:
                print(x)
                user.groups.add(x)
            messages.success(request, 'Account was created for' + username)
            return redirect('dot_adduser')
    return render(request, "add_user.html",{'form':form})

@login_required(login_url="/login")
def dot_groups(request):
    gp = Group.objects.all()
    return render(request, "groups.html",{'b':gp})

@login_required(login_url="/login")
def dot_add_groups(request):
    if request.method == 'POST':
        name = request.POST['g_name']
        if name != '':
            if len(Group.objects.filter(name=name)) == 0:
                gp = Group(name=name)
                gp.save()
    return redirect('dot_groups')

@login_required(login_url="/login")
def dot_viewusers(request):
        user = request.user
        if user.is_superuser:
            u= User.objects.filter(is_superuser = '0')
            g= user.groups.filter(user=user.id)
            print(g)
            for x in g:
                print(x.group.name)
            return render(request, "viewusers.html",{'user':u})
        else:
            u= User.objects.filter(is_superuser = '0',username =user)
            return render(request, "viewusers.html",{'user':u})
        
@login_required(login_url="/login")
def dot_add_groups_permissions(request):
    g_id = request.GET['a']
    gp = Group.objects.all().filter(id=g_id)
    perms = Permission.objects.all()
    return render(request, "groupperms.html",{'gp':gp, 'perms':perms})

#hoteladmin add hotels
@login_required(login_url="/login")
def dot_addhotel(request):
    form = AddHotelsForm
    h_type=hotel_type.objects.all()
    ctry=country.objects.all()
    st=state.objects.all()
    cty=city.objects.all()
    org=organization.objects.all()
    return render(request,'addhotels.html',{'form':form,'country':ctry,'states':st,'city':cty,'organization':org,'hotel_type':h_type})

# add hotels
def dot_addhoteldb(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username,password=password)
        print(user.id)
        name = request.POST['name']
        contact_person = request.POST['contact_person']
        phone= request.POST['phone']
        address = request.POST['address']
        cotry_id = request.POST['country'] 
        sts_id = request.POST['state']
        citi_id = request.POST['city']
        status = request.POST['status']
        organtn_id = request.POST['organization']
        gr_id = request.POST.getlist('groups')
        cnty = country.objects.all().filter(id=cotry_id)
        sts = state.objects.all().filter(id=sts_id)
        citi = city.objects.all().filter(id=citi_id)
        for x in  gr_id:
                print(x)
                user.groups.add(x)
        hotl = userprofile(user_id=user.id,name=name, organization_id=organtn_id, contact_person=contact_person, phone=phone, address=address, country=cnty[0].name, state=sts[0].name, city=citi[0].name,status=status)
        hotl.save()
    return redirect('dot_addhotel')



# # add hotel_staffs
# def dot_add_staffdb(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = User.objects.create_user(username=username,password=password)
#         print(user.id)
#         name = request.POST['name']
#         phone= request.POST['phone']
#         address = request.POST['address']
#         status = request.POST['status']
#         departmt= request.POST['department']
#         gr_id = request.POST.getlist('groups') 
#         dept = staff_department.objects.all().filter(id=departmt)     
#         for x in  gr_id:
#                 print(x)
#                 user.groups.add(x)
#         stff = userprofile(user_id=user.id,name=name, phone=phone, address=address,department_id=dept[0].department,status=status)
#         stff.save()
#     return redirect('dot_add_staff')

# @login_required(login_url="/login")
# def dot_addhotel(request):
#     form = AddHotel_staffForm
#     dept=staff_department.objects.all()
#     return render(request,'add_hotelstaff.html',{'form':form,'department':dept})



# view hotels
def dot_viewhotels(request):
    upro= userprofile.objects.all()
    return render(request, "viewhotels.html",{'hotel':upro})


#edit hotel
@login_required(login_url="/login")
def dot_edit_hotel(request):
    ed_id = request.GET['a']
    print(ed_id)
    htl = userprofile.objects.all().filter(id=ed_id)
    return render(request, "edit_hotel.html",{'htl':htl})

@login_required(login_url="/login")
def dot_edit_hoteldb(request):
    return render(request, "edit_hotel.html")


#delete hotel
@login_required(login_url="/login")
def delete_hotel(request):
    d_id = request.GET['d_id']
    print(d_id)
    htl = userprofile.objects.all().filter(id=d_id)
    print(htl[0].user.id)
    User.objects.all().filter(id=htl[0].user.id).delete()
    htl.delete()
    dat = ['hotel deleted']
    return JsonResponse(dat, safe=False)

# update hotel
def dot_update_hotel(request):
    if request.method == 'POST':
        # contact_person = request.POST['contact_person']
        phone= request.POST['phone']
        name = request.POST['name']
        password = request.POST['pwd']
        address = request.POST['address']
        h_type_id = request.POST['hotel_type']
        cotry_id = request.POST['country'] 
        sts_id = request.POST['state']
        citi_id = request.POST['city']
        organtn_id = request.POST['organization']
        h_type = hotel_type.objects.all().filter(id=h_type_id)
        cnty = country.objects.all().filter(id=cotry_id)
        sts = state.objects.all().filter(id=sts_id)
        citi = city.objects.all().filter(id=citi_id)
        ho = User(username=name, password=password)
        user_id = userprofile.objects.all().filter(id=user_id)
        ho.save()
        print(ho.id) 
        if int(id[0].c_user) == User.id or User.is_superuser:
            userprofile.objects.all().filter(id=id).update( organization_id=organtn_id, phone=phone, address=address,hotel_type=h_type[0].types, country=cnty[0].name, state=sts[0].name, city=citi[0].name)
        # hotl.save()
        # if int(dn_ar[0].c_user) == user.id or user.is_superuser:
        #     destination_area.objects.all().filter(id=da_id).update(name=destn_area, place=place, longitude=longitude, lattitude=lattitude, status=status)
        # else:
        #     messages.success(request, f"you are not autherized to edit !!!!!  ")

    return redirect('dot_viewhotels')


#ajax get country
@login_required(login_url="/login")
def ajax_country(request):
        c_id = request.GET['country']
        print(c_id)
        sts = state.objects.all().filter(country_id=c_id)
        dat = []
        for x in sts:
            dat.append({'name':x.name, 'id':x.id})
            print(dat)
        return JsonResponse(dat, safe=False)


#ajax get states
@login_required(login_url="/login")
def ajax_state(request):
    s_id = request.GET['state']
    cit = city.objects.all().filter(state_id=s_id)
    dat = []
    for x in cit:
        dat.append({'name':x.name, 'id':x.id})
        print(dat)
    return JsonResponse(dat, safe=False)

#add destinstion area template display
@login_required(login_url="/login")
def dot_destination_area(request):
    cntry = country.objects.all()
    stat = state.objects.all()
    return render(request, "destinationarea.html",{'country':cntry, 'state':stat})

#save destinatin area to database
@login_required(login_url="/login")
def dot_add_destination_area(request):
    if request.method == 'POST':
        user = request.user.id
        destn_area = request.POST['destn_area']
        place = request.POST['place']
        statu = request.POST['status']
        cuntry_id = request.POST['country']
        state_id = request.POST['state']
        coutry = country.objects.all().filter(id = cuntry_id)
        stat = state.objects.all().filter(id = state_id)
        lattitude = request.POST['lattitude']
        longitude = request.POST['longitude']
        d_area = destination_area(name=destn_area, place=place, status=statu, country=coutry[0].name, state=stat[0].name, lattitude=lattitude, longitude=longitude, c_user=user)
        d_area.save()
    return redirect("dot_destination_area")

#edit destination area
@login_required(login_url="/login")
def dot_edit_destinationarea(request):
    # user = request.user.id
    ed_id = request.GET['a']
    destn = destination_area.objects.all().filter(id=ed_id)
    # if int(destn[0].c_user) == user:
    #     pass
    return render(request, "edit_destinationarea.html",{'destn':destn})

from django.contrib import messages
def dot_update_destinationarea(request):
    if request.method == 'POST':
        user = request.user
        print(user.id)
        da_id = request.POST['da_id']
        destn_area = request.POST['destn_area']
        place = request.POST['place']
        lattitude = request.POST['lattitude']
        longitude = request.POST['longitude']
        status = request.POST['status']
        dn_ar = destination_area.objects.all().filter(id=da_id)
        
        if int(dn_ar[0].c_user) == user.id or user.is_superuser:
            destination_area.objects.all().filter(id=da_id).update(name=destn_area, place=place, longitude=longitude, lattitude=lattitude, status=status)
        else:
            messages.success(request, f"you are not autherized to edit !!!!!  ")

    return redirect("dot_view_destinationarea")
#delete destination area
@login_required(login_url="/login")
def delete_darea(request):
    user = request.user
    d_id = request.GET['d_id']
    destn = destination_area.objects.all().filter(id=d_id)
    dat = []
    if int(destn[0].c_user) == user.id or user.is_superuser:
        destn.delete()
        dat.append('deleted')
    else:
        dat.append("can't delete")
    
    return JsonResponse(dat, safe=False)

#view destination area list
@login_required(login_url="/login")
def dot_view_destinationarea(request):
    destn_area = destination_area.objects.all()
    return render(request, "view_destinationarea.html",{'destn_area':destn_area})

#add destination template
@login_required(login_url="/login")
def dot_destinations(request):
    destn_area = destination_area.objects.all()
    return render(request, "add_destinations.html",{'destn_area':destn_area})

#save destination to database 
@login_required(login_url="/login")
def dot_add_destination(request):
    if request.method ==  'POST':
        user = request.user.id
        destn = request.POST['destn']
        destn_area = request.POST['destn_area']
        img = request.FILES.getlist('image')
        address = request.POST['address']
        description = request.POST['description']
        climate = request.POST['climate']
        culture = request.POST['culture']
        lattitude = request.POST['lattitude']
        longitude = request.POST['longitude']
        dstn = destinstions(name=destn, d_area_id=destn_area, address=address, description=description, climate=climate, culture=culture, longitude=longitude, lattitude=lattitude, c_user=user)
        dstn.save()
        for x in img:
            b=destination_img(destinstions_id=dstn.id, image=x)
            b.save()
    return redirect("dot_destinations")

#view destination list
@login_required(login_url="/login")
def dot_view_destination(request):
    destn = destinstions.objects.all()
    destn_list=[]
    for x in destn:
        img= destination_img.objects.all().filter(destinstions=x.id)
        im =''
        if img:
            im = img[0].image
        destn_list.append({'id':x.id, 'name':x.name,'address':x.address , 'description':x.description,'climate':x.climate,'culture':x.culture, 'image':im, 'd_area':x.d_area.name})
    return render(request, "view_destination.html",{'destn_list':destn_list})

@login_required(login_url="/login")
def delete_destination(request):
    user = request.user
    d_id = request.GET['d_id']
    destn = destinstions.objects.all().filter(id=d_id)
    if int(destn[0].c_user) == user.id or user.is_superuser:
        destn.delete()
    else:
        pass
    dat = ['Destination area deleted']
    return JsonResponse(dat, safe=False)  

@login_required(login_url="/login")
def dot_editdestination(request):
    e_id = request.GET['a']
    destn = destinstions.objects.all().filter(id=e_id)
    img = destination_img.objects.all().filter(destinstions=e_id)
    return render(request, 'edit_destination.html', {'destn':destn, 'img':img})

@login_required(login_url="/login")
def dot_update_destination(request):
    if request.method == 'POST':
        user = request.user
        d_id = request.POST['d_id'] 
        destn_area = request.POST['destn_area']  
        destn = request.POST['destn']     
        address = request.POST['address']
        description = request.POST['description']
        climate = request.POST['climate']
        culture = request.POST['culture']
        lattitude = request.POST['lattitude']
        longitude = request.POST['longitude']
        pic = request.FILES.getlist('image')
        images = request.POST['deletedfiles']
        img = [int(item) for item in images.split(', ') if item.isdigit()]
        length=len(img)  
        count=destination_img.objects.all().filter(destinstions=d_id).count()
        dn = destinstions.objects.all().filter(id=d_id)
        if int(destn[0].c_user) == user.id or user.is_superuser:
            if length < count:
                for x in img:
                    c=destination_img.objects.all().get(id=x)
                    # print(c)
                    if c.image:
                        c.image.delete()
                    c.delete()
                        
            print(count)
            destinstions.objects.all().filter(id=d_id).update(name=destn,  address=address, description=description, climate=climate, culture=culture, longitude=longitude, lattitude=lattitude)
            for x in pic:
                ad_img=destination_img(destinstions_id=d_id, image=x)
                ad_img.save()
        else:
            pass
    return redirect('dot_view_destination')

@login_required(login_url="/login")
def dot_content(request):
    ctnt=content.objects.all()
    print(ctnt)
    return render(request,'content.html',{'content':ctnt})



# API
from  rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status 
from .serializers import customerRegister,destination_areaSerializer,destinstionsSerializer,destination_imgSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
import json
from rest_framework.response import Response
import random 

# def get_data(request):
#     return JsonResponse(data, safe=False)

# Register customers
class Register(APIView):
    def post(self,request,format=None):
        serializer = customerRegister(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='registered'
            data['username']=account.username
            data['first_name']=account.first_name
            data['last_name']=account.last_name
            data['email']=account.email
            data['phone']=account.phone            
            data['cust_type']=account.cust_type
            data['status']=account.status
        else:
            data=serializer.errors
        return Response(data)

# class customerViewset(viewsets.ModelViewSet):
   
# class Register(APIView):
#         queryset = customer.objects.all()
#         queryset = cust_profile.objects.all()
#         serializer_class= customerRegister
#         def post(self,request,format=None):
#             customer_serializer = customerRegister(data=request.data)
#             customer_profile_serializer = cust_profileRegister(data=request.data)
#             data={}
#             if customer_serializer.is_valid() and customer_profile_serializer.is_valid():
#                 customer=customer_serializer.save()
#                 cust_profiledata=customer_profile_serializer.data               
#                 cust_profiledata['username'] = customer.username
#                 cust_profiledata['first_name'] = customer.first_name
#                 cust_profiledata['last_name'] = customer.last_name
#                 cust_profiledata['email'] = customer.email
#                 cust_profiledata['phone'] = customer.phone
#                 profile=cust_profileRegister(data=cust_profiledata)
#                 profile.is_valid(raise_exception=True)
#                 profile.save               
#                 return Response(customer_serializer.errors)
#             else:
#                 data=(customer_profile_serializer.errors)
#             return Response(data)

# cust_profile
# class cust_profileRegister(APIView):
#     def post(self,request,format=None):
#         serializer = cust_profileRegister(data=request.data)
#         profile = {}
#         if serializer.is_valid():
                   
#             account=serializer.save()
#             profile['response'] = 'registered'
#             profile['city'] = account.city
#             profile['state'] = account.state
#             profile['address'] = account.address
#             profile['status'] =account.status
#         else:
#             profile=serializer.errors       
#         return Response(profile)


# login customers(token generation)
class LoginView(APIView):
     def post(self,request):
        cust = json.loads(request.body)
        cust_exist= customer.objects.filter(username=cust['username']).count()
        print(cust_exist)
        if cust_exist>0:
            cust_pass= customer.objects.filter(username=cust['username'], password=cust['password'])
            print(cust_pass)
            for x in cust_pass:
                n= x.id
                print(n)
                if cust_exist:
                    token= str(x.id) + "Token" + str(random.randint(19678999999,29876543210))
                    cus= customer_auth(u_id_id=n, tokens=token)
                    cus.save()
                    return Response({
                        'message':'User logged successfully',
                        'token': token,
                        'user_id' : x.id,
                    })
        else:
            return Response({
             'message':'User does not exist'
            })          


# destination_area
class destination_areaView(viewsets.ModelViewSet):
    queryset=destination_area.objects.all()
    # queryset={destination_area: 'destination_area'}
    # print(queryset)
    serializer_class=destination_areaSerializer

# view destinations
class destinstionsView(viewsets.ModelViewSet):
    queryset=destinstions.objects.all()
    serializer_class=destinstionsSerializer

# destination_img
class destination_imageView(viewsets.ModelViewSet):
    queryset=destination_img.objects.all()
    serializer_class=destination_imgSerializer


# homepage api
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def homepage_contentgreenkitchen(request):
    data ={
    "banners": [
        {
            "url": "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
            "img": "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
            "title": "Banner1",
            "id": 4,           
        },
        {
            "url": "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
            "img": "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
            "title": "Banner1",
            "id": 4,           
        },
        {
            "url": "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
            "img": "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
            "title": "Banner2",
            "id": 4,
            "type": "products"
        },
      
    ],
    "Deal_title": [
        "Today's ",
        "Deals"
    ],
    "Today's_products": [],
    "Exclussive_title": [
    "Exclussive ",
    "Products"
    ],
    "Exclussive_products": [
        {
            "id": 13,
            "title": "RICE",
            "images": [
                "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
            ],
            "Product_variants": [
                {
                    "title": "rice",
                    "id": 100,
                    "price": 60,
                    "original_price": 70
                }
            ]
        },
        {
            "id": 42,
            "title": "TOMATO",
            "images": [
                "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
            ],
            "Product_variants": [
                {
                    "weight": "1 KG",
                    "id": 19,
                    "price": 72,
                    "original_price": 80
                },
                {
                    "weight": "500 gm",
                    "id": 11,
                    "price": 96,
                    "original_price": 100
                }
            ]
        },
        {
            "id": 4,
            "title": "Ladies Finger",
            "images": [
                 "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                 ],
            "Product_variants": [
                {
                    "weight": "1 KG",
                    "id": 7,
                    "price": 90,
                    "original_price": 100
                },
                {
                    "weight": "500 gms",
                    "id": 2,
                    "price": 50,
                    "original_price": 60
                },
                {
                    "weight": "250 gms",
                    "id": 45,
                    "price": 10,
                    "original_price": 20
                }
            ]
        }
    ],
    "Farmfresh_products": [
        {
            "id": 4,
            "title": "Long Bean",
            "images": [
                "https://mygreenkitchen.in/media/cache/sylius_shop_product_thumbnail/05/25/b8f3a84e2a915d0b604b87d994d7.jpeg"
            ],
            "product_variants": [
                {
                    "weight": "1 KG",
                    "id": 1,
                    "price": 80,
                    "original_price": 100
                },
                {
                    "weight": "750 gm",
                    "id": 6,
                    "price": 50,
                    "original_price": 55
                }
            ]
        },
        {
            "id": 11,
            "title": "Cucumber",
            "images": [
                "https://mygreenkitchen.in/media/cache/sylius_shop_product_thumbnail/05/25/b8f3a84e2a915d0b604b87d994d7.jpeg"
            ],
            "product_variants": [
                {
                    "weight": "1 KG",
                    "id": 10,
                    "price": 54,
                    "original_price": 60
                }
            ]
        },
        {
            "id": 12,
            "title": "Green Brinjal",
            "images": [
                "https://mygreenkitchen.in/media/cache/sylius_shop_product_thumbnail/05/25/b8f3a84e2a915d0b604b87d994d7.jpeg"
            ],
            "product_variants": [
                {
                    "weight": "1 KG",
                    "id": 15,
                    "price": 70,
                    "original_price": 74
                },
                {
                    "weight": "500 gms",
                    "id": 20,
                    "price": 49,
                    "original_price": 30
                }
            ]
        },
        {
            "id": 5,
            "title": "Snake Gourd",
            "images": [
                "https://mygreenkitchen.in/media/cache/sylius_shop_product_thumbnail/05/25/b8f3a84e2a915d0b604b87d994d7.jpeg"
            ],
            "Product_variants": [
                {
                    "weight": "1 KG",
                    "id": 5,
                    "price": 70,
                    "original_price": 76
                },
                {
                    "weight": "500 gms",
                    "id": 39,
                    "price": 99,
                    "original_price": 99
                }
            ]
        },
        {
            "id": 6,
            "title": "Bitter Gourd",
            "images": [
                "https://mygreenkitchen.in/media/cache/sylius_shop_product_thumbnail/05/25/b8f3a84e2a915d0b604b87d994d7.jpeg"
            ],
            "product_variants": [
                {
                    "weight": "2 KG",
                    "id": 9,
                    "price": 90,
                    "original_price": 98
                },
                {
                    "weight": "250 gm",
                    "id": 44,
                    "price": 90,
                    "original_price": 94
                }
            ]
        },
    ],
    "New_title": [
        "New ",
        "Products"
    ],
    "New_products": [
        {
            "id": 56,
            "title": "Raw Banana",
            "images": [
                "https://mygreenkitchen.in/media/cache/sylius_shop_product_thumbnail/dd/10/7fce79fb1fefdce6a1229a9fe56e.jpeg"
            ],
            "Product_variants": [
                {
                    "weight": "3 KG",
                    "id": 83,
                    "price": 96,
                    "original_price": 100
                }
            ]
        },
        {
            "id": 68,
            "title": "Mint Leaves",
            "images": [
                "https://mygreenkitchen.in/media/cache/sylius_shop_product_thumbnail/dd/10/7fce79fb1fefdce6a1229a9fe56e.jpeg"
            ],
            "Product_variants": [
                {
                    "weight": "1 Bunch",
                    "id": 98,
                    "price": 80,
                    "original_price": 90
                }
            ]
        },
        {
            "id": 47,
            "title": "Coriander Leaves",
            "images": [
                "https://mygreenkitchen.in/media/cache/sylius_shop_product_thumbnail/dd/10/7fce79fb1fefdce6a1229a9fe56e.jpeg"
            ],
            "product_variants": [
                {
                    "weight": "1 Bunch",
                    "id": 23,
                    "price": 95,
                    "original_price": 100
                }
            ]
        },
        {
            "id": 46,
            "title": "Curry Leaves",
            "images": [
                "https://mygreenkitchen.in/media/cache/sylius_shop_product_thumbnail/dd/10/7fce79fb1fefdce6a1229a9fe56e.jpeg"
            ],
            "Product_variants": [
                {
                    "weight": "1 Bunch",
                    "id": 82,
                    "price": 10,
                    "original_price": 12
                },
                {
                    "weight": "1 KG",
                    "id": 136,
                    "price": 100,
                    "original_price": 120
                }
            ]
        },       
        {
            "id": 31,
            "title": "Ginger",
            "images": [
                "https://mygreenkitchen.in/media/cache/sylius_shop_product_thumbnail/dd/10/7fce79fb1fefdce6a1229a9fe56e.jpeg"
            ],
            "Product_variants": [
                {
                    "weight": "1 KG",
                    "id": 50,
                    "price": 88,
                    "original_price": 100
                },
                {
                    "weight": "500 gms",
                    "id": 52,
                    "price": 44,
                    "original_price": 50
                },
                {
                    "weight": "100 gms",
                    "id": 53,
                    "price": 19,
                    "original_price": 20
                }
            ]
        }
    ],
    "user": "null"
}
    return Response(data)



    #  {"banners":[{
    #     'title': 'welcome to my green kitchen',
    #     'header': 'our products',
    #     'products': ['product1','product2','product3'],
    #     'about': 'about us',
    #     'about_content': 'we are a team of experts in our field and dedicated to providing the best service possible',
    
    # }
    # ]
    # }
    # return Response(data)

    
@api_view(['GET'])
def homepage_contentdot(request):
    data ={
"banner": [
        {
            "title": "India's new trip planner",
            "sub title":"DOT we make your trips more memorable",
            "url": "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
            "img": "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
            "id": 4,           
        },
        
    ],
    
"button": [
        {
            "title": "KARNATAKA",
            "sub title":"10 destinations in Karnataka",          
            "id": 4,           
        },
        
    ],
        "karnataka": [
            {
                
                "id": 13,
                "title": "HUMPI",
                "images": [
                    "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                ],
                "description":" Is a cultural and architectural heritage site built more than 200 years ago. The site was constructed between 1336 AD to 1565 AD. This location is famous for its temples, palaces, market streets and monuments, making up the Vijayanagara Empire.  "
                
            },
            {
                "id": 42,
                "title": "BADAMI",
                "images": [
                    "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                ],
                "description":" It is located in a ravine at the foot of a rugged, red sandstone outcrop that surrounds Agastya lake.  "
            
            },
            {
                "id": 45,
                "title": "MYSORE",
                "images": [
                    "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                    ],
                "description":"  Mysuru has an area of 6,307 sq km and a population of 30,01,127 (2011 census). The city is also known as the City of Palaces, Mysuru has always enchanted its visitors with its quaint charm. "
                
            },
            {
                "id": 43,
                "title": "GOKARNA",
                "images": [
                    "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                    ],
                "description":"  is a small temple town located in Uttara Kannada district of Karnataka state in India, It has a population of around 20,000.  "
                
            }
        ],

     "sub_title_A": [
        "LET US PLAN FOR YOU ",
        "What's next?",
        
    ],
          

            "sub_title1": [
            "NATIONAL PARKS",
            
            ],
    "img": [
       "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
    
    ],
        "national parks": [
            {
                
                "id": 13,
                "title": "JIM CORBETT NATIONAL PARK",
                "images": [
                    "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                ],
                
            },
            {
                "id": 42,
                "title": "GIR NATIONAL PARK",
                "images": [
                    "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                ],
            
            },
            {
                "id": 4,
                "title": "BENNARGETTA NATIONAL PARK",
                "images": [
                    "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                    ],
                
            },
            {
                "id": 4,
                "title": "PERIYAR NATIONAL PARK",
                "images": [
                    "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                    ],
                
            }
        ],
     "sub_title2": [
       "TREKING",
    
    ],
    "img": [
       "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
    
    ],
        "Treking": [
            {
                
                "id": 13,
                "title": "CHOPTA CHANDRASHILA THUNGNATH",
                "images": [
                    "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                ],
                
            },
            {
                "id": 42,
                "title": "CHADAR TREK FROZEN RIVER",
                "images": [
                    "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                ],
            
            },
            {
                "id": 4,
                "title": "AUDENS COL EXPEDITION",
                "images": [
                    "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                    ],
                
            },
            {
                "id": 4,
                "title": "BINSAR WEEKEND TREK",
                "images": [
                    "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                    ],
                
            }
        ],
     "sub_title3": [
       "HILLSTATION",
    
    ],
    "img": [
       "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
    
    ],
        "Hillstations": [
            {
                
                "id": 13,
                "title": " Shimla",
                "images": [
                    "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                ],
                
            },
            {
                "id": 42,
                "title": "Ooty",
                "images": [
                    "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                ],
            
            },
            {
                "id": 4,
                "title": "Srinagar",
                "images": [
                    "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                    ],
                
            },
            {
                "id": 4,
                "title": " Coorg",
                "images": [
                    "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                    ],
                
            }
        ],
     "sub_title4": [
       "HONEYMOON",
    
    ],
    "img": [
       "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
    
    ],
        "Honeymoon": [
            {
                
                "id": 13,
                "title": "GOA",
                "images": [
                    "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                ],
                
            },
            {
                "id": 42,
                "title": "ANDAMAN",
                "images": [
                    "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                ],
            
            },
            {
                "id": 4,
                "title": "HIMACHAL",
                "images": [
                    "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                    ],
                
            },
            {
                "id": 4,
                "title": "KASHMIR",
                "images": [
                    "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                    ],
                
            }
        ],


    "sub_title_B": [
         "Seasonal suggestions",
         "WHERE TO NEXT?",
    ],
        "sub_title5": [
            "HIMACHAL PRADESH",
        
        ],
            "img": [
            "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
            
            ],
            "himachal pradesh": [
                {
                    
                    "id": 13,
                    "title": "manali",
                    "images": [
                        "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                    ],
                    
                },
                {
                    "id": 42,
                    "title": "Dharamshala",
                    "images": [
                        "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                    ],
                
                },
                {
                    "id": 4,
                    "title": "Dalhousie",
                    "images": [
                        "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                        ],
                    
                },
                {
                    "id": 4,
                    "title": "Kasol",
                    "images": [
                        "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                        ],
                    
                }
        ],
        "sub_title6": [
            "OOTY",  
        ],
            "img": [
            "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
            
            ],
            "Ooty": [
                {
                    
                    "id": 13,
                    "title": "Government Rose Garden",
                    "images": [
                        "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                    ],
                    
                },
                {
                    "id": 42,
                    "title": "Tamilnadu Tourism Ooty Boat House",
                    "images": [
                        "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                    ],
                
                },
                {
                    "id": 4,
                    "title": "Mudumalai Tiger Reserve",
                    "images": [
                        "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                        ],
                    
                },
                {
                    "id": 4,
                    "title": "Doddabetta Peak",
                    "images": [
                        "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                        ],
                    
                }
            ],

     "sub_title7": [
       "MANALI",
    
    ],
        "img": [
        "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
        
        ],
            "Manali": [
                {
                    
                    "id": 13,
                    "title": " Hadimba Devi Temple",
                    "images": [
                        "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                    ],
                    
                },
                {
                    "id": 42,
                    "title": "Old Manali",
                    "images": [
                        "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                    ],
                
                },
                {
                    "id": 4,
                    "title": "Museum of Himachal Culture & Folk Art",
                    "images": [
                        "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                        ],
                    
                },
                {
                    "id": 4,
                    "title": " Rohtang La",
                    "images": [
                        "https://mygreenkitchen.in/assets/shop/img/mgk_veg.jpg",
                        ],
                    
                }
            ],
            

    
    "sub_title_C": [
         " DOT MEMBERSHIP CARD"
        
    ],
        "card" : [
            {
                "id": 56,
                "title": "MORE ABOUT DOT MEMBERSHIP CARD",
                "images": [
                    "https://mygreenkitchen.in/media/cache/sylius_shop_product_thumbnail/dd/10/7fce79fb1fefdce6a1229a9fe56e.jpeg"
                ],
            
            },
            
        ],


    "sub_title_D": [
        "PICK THE BEST",
        "TOP STAYS",
        
        
    ],    
                "stays": [
                    {
                        "id": 56,
                        "title": "WANDERLUST HUMPI",
                        "facility": "3 beds,2 bedrooms",
                        "price":"35004/night",
                        "images": [
                            "https://mygreenkitchen.in/media/cache/sylius_shop_product_thumbnail/dd/10/7fce79fb1fefdce6a1229a9fe56e.jpeg"
                        ],

                    },
                    {
                        "id": 50,
                        "title": "Waterfall guest house",
                        "facility": "3 beds,2 bedrooms",
                        "price":"4679/night",
                        "images": [
                            "https://mygreenkitchen.in/media/cache/sylius_shop_product_thumbnail/dd/10/7fce79fb1fefdce6a1229a9fe56e.jpeg"
                        ],
                    },
                    {
                        "id": 57,
                        "title": "Wild Stone Humpi",
                        "facility": "3beds,2 bedrooms",
                        "price":"4679/night",
                        "images": [
                            "https://mygreenkitchen.in/media/cache/sylius_shop_product_thumbnail/dd/10/7fce79fb1fefdce6a1229a9fe56e.jpeg"
                        ],
                    },
                    {
                        "id": 59,
                        "title": "Hakuna matata Inn",
                        "facility": "3beds,2 bedrooms",
                        "price":"4679/night",
                        "images": [
                            "https://mygreenkitchen.in/media/cache/sylius_shop_product_thumbnail/dd/10/7fce79fb1fefdce6a1229a9fe56e.jpeg"
                        ],
                    },
                ],
    "sub_title_E": [
        "DOT EXCLUSIVE",   
        "Discover travel memories",      
    ], 
            "things": [
                {
                    "id": 5,
                    "title": "14 best things to do in Humpi",
                    "images": [
                        "https://mygreenkitchen.in/media/cache/sylius_shop_product_thumbnail/dd/10/7fce79fb1fefdce6a1229a9fe56e.jpeg"
                    ],

                },
                {
                    "id": 6,
                    "title": "Top destinations for food and drink",
                    "images": [
                        "https://mygreenkitchen.in/media/cache/sylius_shop_product_thumbnail/dd/10/7fce79fb1fefdce6a1229a9fe56e.jpeg"
                    ],
                
                },
                
                ],
            
        
  "user": "null"
},
    return Response(data)


