from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import update_session_auth_hash
from .form import RegisterForm,AddHotelsForm, FacilitytypeForm, EntrollmentForm
from django.http import JsonResponse
from django.contrib import messages



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
                messages.info(request, {username}) 
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
    
    # if request.user.groups.filter(name='marketing').exists():
    #     form = Register
    # else:
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
            usr= User.objects.filter(is_superuser = '0')     
            user_groups = request.user.groups.all()
            # g= user.groups.filter(user=user.id)
            # print(g)
            for x in user_groups:
                print(x.name)
            return render(request, "viewusers.html",{'user':usr})
        else:
            u= User.objects.filter(is_superuser = '0').exclude(username=user)
            return render(request, "viewusers.html",{'user':u})


@login_required(login_url="/login")
def dot_edit_user(request):
    ur_id = request.GET['a']
    usr = User.objects.all().filter(id=ur_id)
    print(usr)
    return render(request, "edituser.html",{'user':usr})

        
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

@login_required(login_url="/login")
def dot_addhoteldb(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        print(user.id)
        # h_type_id = request.POST['hotel_type']
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
        # h_type = hotel_type.objects.all().filter(id=h_type_id)
        cnty = country.objects.all().filter(id=cotry_id)
        sts = state.objects.all().filter(id=sts_id)
        citi = city.objects.all().filter(id=citi_id)
            # password = 'PASSWORD_HERE'
            # form = AddHotelsForm
            # if request.method == "POST":
            #     form = AddHotelsForm(request.POST)
            # if form.is_valid():
            #     user = form.save()
            #     name = form.cleaned_data.get('username')
            #     print(name)
            # if form.is_valid():
            #     user = form.save()
            # form.password = make_password(password)
            # form.save()
            # ho = User(username=name, password=password)
            # ho.save()
            # print(ho.id) 
            # gr_id = request.POST.getlist('groups')
            # idd= gr_id[0]
            # print(gr_id)
        for x in  gr_id:
                print(x)
                user.groups.add(x)
        hotl = userprofile(user_id=user.id,name=name, organization_id=organtn_id, contact_person=contact_person, phone=phone, address=address, country=cnty[0].name, state=sts[0].name, city=citi[0].name,status=status)
        hotl.save()

    return redirect('dot_addhotel')

# view hotels
@login_required(login_url="/login")
def dot_viewhotels(request):
    upro= userprofile.objects.all().filter(organization=1)
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
        ho_id = request.POST['ho_id']
        print(ho_id)
        name = request.POST['name']
        contact_person = request.POST['contact_person']
        phone= request.POST['phone']
        address = request.POST['address']
        print(address)
        cotry = request.POST['country'] 
        sts = request.POST['state']
        citi = request.POST['city']
        organtn_id = request.POST['organization']
        # h_type = hotel_type.objects.all().filter(id=h_type_id)
        # cnty = country.objects.all().filter(id=cotry_id)
        # sts = state.objects.all().filter(id=sts_id)
        # citi = city.objects.all().filter(id=citi_id)
        userprofile.objects.all().filter(id=ho_id).update(name=name,contact_person=contact_person, phone=phone, address=address, country=cotry, state=sts, city=citi)
        # hotl.save()
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
            messages.error(request, "You are not autherized to edit !!!!")

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
        # print(x.d_area.name)
        img= destination_img.objects.all().filter(destinstions=x.id)
        # print('>>>>>>>>>>>>>>')
        # print(img[0].id)
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
        if int(dn[0].c_user) == user.id or user.is_superuser:
            if length < count:
                for x in img:
                    c=destination_img.objects.all().get(id=x)
                    # print(c)
                    if c.image:
                        c.image.delete()
                    c.delete()           
            # print(count)
            destinstions.objects.all().filter(id=d_id).update(name=destn,  address=address, description=description, climate=climate, culture=culture, longitude=longitude, lattitude=lattitude)
            for x in pic:
                ad_img=destination_img(destinstions_id=d_id, image=x)
                ad_img.save()
        else:
            messages.error(request, "You are not autherized to edit !!!!")
    return redirect('dot_view_destination')

@login_required(login_url="/login")
def dot_addorganization(request):
    form = EntrollmentForm 
    destn = destinstions.objects.all()
    stat = state.objects.all()
    citi = city.objects.all()
    return render(request,'organizations.html',{'destn':destn, 'stat':stat, 'citi':citi, 'form':form})


@login_required(login_url="/login")
def dot_addorganization_db(request):
    if request.method == 'POST':
        user = request.user.id
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user_or = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
        title = request.POST['title']
        org_type = request.POST['org_type']
        destn = request.POST['destn']
        contact_person = request.POST['contact_person']
        contact_number = request.POST['contact_number']
        website = request.POST['website']
        sts_id = request.POST['state']
        city_id = request.POST['city']
        address = request.POST['address']
        proof = request.POST['proof']
        status = request.POST['status']
        img = request.FILES.getlist('image')
        # stat = state.objects.all().filter(id=sts_id)      
        # citi = city.objects.all().filter(id=city_id)
        user_or.groups.add(3)
        org = organization(title=title, org_type=org_type, destinstion_id=destn, contact_person=contact_person, contact_number=contact_number, website=website,
         state_id=sts_id, city_id=city_id, address=address, email=email, proof=proof, status=status, c_user=user, user_id=user_or.id)
        org.save()
        for x in img:
            or_img=organization_images(organization_id=org.id, images=x)
            or_img.save()
        
        return redirect('dot_organizationlist')


@login_required(login_url="/login")
def dot_organizationlist(request):
    org = organization.objects.all()
    orgstn = []
    for x in org:
        # print(x.d_area.name)
        img= organization_images.objects.all().filter(organization=x.id)
        # print('>>>>>>>>>>>>>>')
        # print(img[0].id)
        im =''
        if img:
            im = img[0].images
        orgstn.append({'id':x.id, 'title':x.title,'org_type':x.org_type , 'detn_name':x.destinstion.name,'contact_person':x.contact_person,'contact_number':x.contact_number, 'website':x.website,
         'address':x.address, 'email':x.email, 'state':x.state, 'city':x.city, 'proof':x.proof, 'status':x.status, 'image':im,})
    return render(request, "organizationlist.html",{'org':orgstn})


@login_required(login_url="/login")
def dot_edite_organization(request):
    org_id = request.GET['a']  
    orgn = organization.objects.all().filter(id=org_id)
    img = organization_images.objects.all().filter(organization=org_id)
    destn = destinstions.objects.all()
    stat = state.objects.all()
    citi = city.objects.all()
    orgn_user = User.objects.all().filter(id=orgn[0].user_id)
    return render(request, 'editOrganization.html', {'orgn':orgn, 'destn':destn, 'stat':stat, 'citi':citi, 'img':img, 'orgn_user':orgn_user})


@login_required(login_url="/login")
def dot_updateorganization(request):
    if request.method == 'POST':
        user = request.user
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        or_id = request.POST['or_id']
        title = request.POST['title']
        org_type = request.POST['org_type']
        destn = request.POST['destn']
        # print(destn)
        contact_person = request.POST['contact_person']
        contact_number = request.POST['contact_number']
        website = request.POST['website']
        email = request.POST['email']
        state = request.POST['state']
        city = request.POST['city']
        # print(state)
        # print(city)
        address = request.POST['address']
        proof = request.POST['proof']
        img = request.FILES.getlist('image')
        status = request.POST['status']
        deletedimg = request.POST['deletedfiles']
        orgatn = organization.objects.filter(id=or_id)
        usr = User.objects.get(id=orgatn[0].user_id)
        if int(orgatn[0].c_user) == user.id or user.is_superuser:
            if User.objects.filter(username=username).exclude(id=orgatn[0].user_id).exists():             
                messages.error(request, 'Username already exists')
                return redirect('dot_organizationlist')
            else:
                usr.username = username
                usr.first_name = first_name
                usr.last_name = last_name
                usr.email = email
                usr.save()
                orgatn.update(title=title, org_type=org_type, destinstion_id=destn, contact_person=contact_person, contact_number=contact_number, website=website,
                state=state, city=city, address=address, email=email, proof=proof, status=status)
                for x in img:
                        ad_img=organization_images(organization_id=or_id, images=x)
                        ad_img.save()
                img = [int(item) for item in deletedimg.split(', ') if item.isdigit()]
                length=len(img) 
                count=organization_images.objects.all().filter(organization_id=or_id).count() 
                print(count)
                if length < count:
                        for x in img:
                            c=organization_images.objects.all().get(id=x)
                            print(c)
                            if c.images:
                                # pass
                                c.images.delete()
                            c.delete()
        else:
            messages.error(request, "You can't delete all images !!!!")
    else:
        messages.error(request, "You are not autherized to edit !!!!")

    return redirect('dot_organizationlist')


@login_required(login_url="/login")
def delete_organization(request):
    org_id = request.GET['org_id']
    print(org_id)
    orgtn = organization.objects.all().filter(id=org_id)
    organization_images.objects.all().filter(organization_id=org_id)
    # orgtn.delete()
    dat = {'msg':'organization deleted'}
    return JsonResponse(dat, safe=False)

@login_required(login_url="/login")
def dot_addfacilitytype(request):  
    if request.method == 'POST':
        form = FacilitytypeForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            status = form.cleaned_data['status']
            print(status)
            faclty_typ = facility_type(title=title, description=description, status=status)
            faclty_typ.save()
            return redirect('dot_viewfacilitytype')

    else:
        form = FacilitytypeForm
    return render(request,'facilitytype.html',{'form':form})

@login_required(login_url="/login")
def dot_viewfacilitytype(request):
    faclty_type = facility_type.objects.all()
    return render(request,'viewfacilitytype.html',{'faclty_type':faclty_type})

@login_required(login_url="/login")
def dot_edit_facilitytype(request):
    faclity_type_id = request.GET['a']
    print(faclity_type_id)
    faclty_type = facility_type.objects.all().filter(id=faclity_type_id)
    print(faclty_type)

    return render(request,'editfacilitytype.html',{'faclty_type':faclty_type})

@login_required(login_url="/login")
def dot_addfacility(request):
    faclty_type = facility_type.objects.all()
    destn = destinstions.objects.all()
    orgtn = organization.objects.all()
    return render(request,'facility.html',{'faclty_type':faclty_type, 'destn':destn, 'orgtn':orgtn})

@login_required(login_url="/login")
def dot_addfacilitydb(request):
    if request.method == 'POST':
        user_id = request.user.id
        destn = request.POST['destn']
        typ = request.POST['typ']
        # organization = request.POST['organization']
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        img = request.FILES.getlist('image')
        status = request.POST['status']
        orgtn_id = organization.objects.all().filter(user_id=user_id)
        # print(orgtn_id)
        # print(destn)
        faclty = destn_facility(destinstions_id=destn, orgatn_id=orgtn_id[0].id, title=title, description=description, types=typ, amount=price, status=status)
        faclty.save()
        for x in img:
            f_image=facility_image(destinstion_id=destn, image=x, facility_id=faclty.id, status=status, imagetype='facility')
            f_image.save()


    return redirect('dot_viewfacilitylist')

@login_required(login_url="/login")
def dot_viewfacilitylist(request):
    destn_facilty = destn_facility.objects.all()
    fclty_list = []
    for x in destn_facilty:  
        img= facility_image.objects.all().filter(facility_id=x.id)
        im = ''
        # print(img[0].imagetype)
        if im:
            im = img[0].image
            
        fclty_list.append({'id':x.id, 'destinstion':x.destinstions.name, 'types':x.types, 'title':x.title, 'description':x.description,
            'amount':x.amount, 'status':x.status, 'image':img[0].image})
    # print(fclty_list)
    return render(request, 'viewfacilitylist.html',{'destn_facilty':fclty_list})



#  org = organization.objects.all()
#     orgstn = []
#     for x in org:
#         # print(x.d_area.name)
#         img= organization_images.objects.all().filter(organization=x.id)
#         # print('>>>>>>>>>>>>>>')
#         # print(img[0].id)
#         im =''
#         if img:
#             im = img[0].images
#         orgstn.append({'id':x.id, 'title':x.title,'org_type':x.org_type , 'detn_name':x.destinstion.name,'contact_person':x.contact_person,'contact_number':x.contact_number, 'website':x.website,
#          'address':x.address, 'email':x.email, 'state':x.state, 'city':x.city, 'proof':x.proof, 'status':x.status, 'image':im,})
#     return render(request, "organizationlist.html",{'org':orgstn})

@login_required(login_url="/login")
def dot_delete_organization(request):
    faclty_id = request.GET['a']
    faclty = destn_facility.objects.all().filter(id=faclty_id)
    facility_image.objects.all().filter(facility=faclty_id).delete()
    faclty.delete()
    return redirect('dot_viewfacilitylist')


def dot_orderlist(request):
    return render(request, 'orderlist.html')

def dot_bookinglist(request):
    return render(request, 'bookinglist.html')


@login_required(login_url="/login")
def dot_content(request):
    ctnt=content.objects.all()
    print(ctnt)
    return render(request,'content.html',{'content':ctnt})