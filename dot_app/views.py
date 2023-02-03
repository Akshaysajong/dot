from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import update_session_auth_hash
from .form import RegisterForm,AddHotelsForm
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
from django.contrib.auth.hashers import make_password


@login_required(login_url="/login")
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
        # contact_person = request.POST['contact_person']
        phone= request.POST['phone']
        ho_id = request.POST['ho_id']
        print(ho_id)
        name = request.POST['name']
        contact_person = request.POST['contact_person']
        phone= request.POST['phone']
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
        img = request.FILES.getlist('image')
        description = request.POST['description']
        statu = request.POST['status']
        cuntry_id = request.POST['country']
        state_id = request.POST['state']
        coutry = country.objects.all().filter(id = cuntry_id)
        stat = state.objects.all().filter(id = state_id)
        lattitude = request.POST['lattitude']
        longitude = request.POST['longitude']
        d_area = destination_area(name=destn_area, place=place,description=description, status=statu, country=coutry[0].name, state=stat[0].name, lattitude=lattitude, longitude=longitude, c_user=user, image=img)
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
        destn_type = request.POST['destn_type']
        dstn = destinstions(name=destn, d_area_id=destn_area, address=address, description=description, climate=climate, culture=culture, longitude=longitude, lattitude=lattitude, c_user=user ,destn_type=destn_type)
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



# API
from  rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status 
from .serializers import customerRegister,bannerSerializer,destinationsSerializer,destination_imgSerializer,placesSerializer,staysSerializer,staysimgSerializer,bestthingsSerializer,cardSerializer,destinationdetailsSerializer,destinationdetails_imgSerializer,destination_humpidetailsSerializer,destination_humpidetails_imgSerializer,destination_humpidescription_Serializer,humpi_surroundingsSerializer,humpi_surroundings_imgSerializer,stay_humpiSearializer,stay_humpi_imgSerializer
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
            data['name']=account.name
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
        cust_exist= customer.objects.filter(name=cust['name']).count()
        print(cust_exist)
        if cust_exist>0:
            cust_pass= customer.objects.filter(name=cust['name'], pwd=cust['pwd'])
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


# # destination_area
# class destination_areaView(viewsets.ModelViewSet):
#     queryset=destination_area.objects.all()
#     # queryset={destination_area: 'destination_area'}
#     # print(queryset)
#     serializer_class=destination_areaSerializer

# # view destinations
# class destinstionsView(viewsets.ModelViewSet):
#     queryset=destinstions.objects.all()
#     serializer_class=destinstionsSerializer

# # destination_img
# class destination_imageView(viewsets.ModelViewSet):
#     queryset=destination_img.objects.all()
#     serializer_class=destination_imgSerializer



class dot_homepageAPI(APIView):
    def get(self, request):
        ctnt=content.objects.all()
        dest=destinstions.objects.all()
        dest_img=destination_img.objects.all()
        places=destination_area.objects.all()
        # places_img=destination_area.objects.all()
        cards=card.objects.all()
        stays=organization.objects.all()
        stays_img=organization_images.objects.all()
        best_thgs=best_things.objects.all()
       

        content_data=bannerSerializer(ctnt,many=True).data
        destinations_data=destinationsSerializer(dest, many=True).data
        destination_img_data=destination_imgSerializer(dest_img, many=True).data
        places_data=placesSerializer(places, many=True).data
        # places_img_data=places_imgSerializer(places_img, many=True).data
        card_data=cardSerializer(cards,many=True).data
        stays_data=staysSerializer(stays, many=True).data
        stays_img_data=staysimgSerializer(stays_img,many=True).data
        best_thgs_data=bestthingsSerializer(best_thgs, many=True).data
        titleA1 = {'title':'LET US PLAN FOR YOU '}
        titleA2 = {'title':' What is next?'}
        titleB1 = {'title':'SEASONAL SUGGESTIONS '}
        titleB2 = {'title':'Where to next?'}
        titleC1 = {'title':'PICK THE BEST'}
        titleC2 = {'title':'Top stays'}
        titleD1 = {'title':'DOT EXCLUSIVE Discover'}
        titleD2 = {'title':'travel memories'}

        
        data = {
            'banner':content_data,
            'destination title1':[titleA1],
            'destination title2':[titleA2],   
            'destinations':destinations_data,           
            'destination_img':destination_img_data,
            'place title1':[titleB1],
            'place title2':[titleB2],
            'places':places_data,
            # 'places_img':places_img_data,
            'DOTcard':card_data,
            'stays title1':[titleC1],
            'stays title2':[titleC2],
            'stays':stays_data,
            'stays_img':stays_img_data,
            'things title1':[titleD1],
            'things title2':[titleD2],
            'best_thgs':best_thgs_data,
           
        }
        return Response(data)


# button
class dot_destination_detailsAPI(APIView):
    def get(self, request):
        destn=destination_area.objects.all().filter(name='karnataka')
        dest_img=destination_img.objects.all()

        destn_data=destinationdetailsSerializer(destn,many=True).data        
        destn_img_data=destinationdetails_imgSerializer(dest_img, many=True).data 
        title1 = {'title':'KARNATAKA'}

 
        data = {
            'destination title':[title1],   
            'destinations':destn_data,           
            'destination_img':destn_img_data,
             }
        return Response(data)

# humpi
class dot_destination_humpidetailsAPI(APIView):
    def get(self, request):
        dest_img=destination_img.objects.all().filter(id=7)
        destn=destinstions.objects.all().filter(name='hampi')
        destn_description=destinstions.objects.all().filter(id=7)
        humpi_surroundings=destinstions.objects.all().filter(d_area_id=3)
        humpi_surroundings_img = []
        for x in humpi_surroundings:    
            img=destination_img.objects.all().filter(destinstions_id=x.id)
            im = ''
            if im:
                im = img[0].image
            humpi_surroundings_img.append({'id':x.id, 'image':img[0].image})  
        stay=organization.objects.all()
        stays_img=organization_images.objects.all()

        destn_data=destination_humpidetailsSerializer(destn,many=True).data        
        destn_img_data=destination_humpidetails_imgSerializer(dest_img, many=True).data 
        destn_description_data=destination_humpidescription_Serializer(destn_description, many=True).data
        humpi_surroundings_data=humpi_surroundingsSerializer(humpi_surroundings, many=True).data
        humpi_surroundings_img_data=humpi_surroundings_imgSerializer(humpi_surroundings_img,many=True).data
        stay_data=stay_humpiSearializer(stay, many=True).data  
        stays_img_data=stay_humpi_imgSerializer(stays_img, many=True).data
        title1 = {'title':'KARNATAKA'}
        title2 = {'title':'Hampi'}
        title3 = {'title':'Discover the sorroundings'}
        title4 = {'title':'Plan your trip'}
        title5 = {'title':'Find your stay '}
        title6 = {'title':'Experiences'}
        

        data = {
            # 'destination title':[title1],
            # 'destinations':destn_data,           
            'banner_hampi':destn_img_data,
            'destination title':[title1],
            'destination title2':[title2],
            
            
            'humpi_description':destn_description_data,
            'destination title3':[title3],
            'humpi_surroundings':humpi_surroundings_data,
            'humpi_surroundings_img':humpi_surroundings_img_data,
            'destination title4':[title4],
            'destination title5':[title5],
            'stay':stay_data,
            'stays_img':stays_img_data,
            'destination title6':[title6],

             }
        return Response(data)






# search autocomplete API

# from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets,filters
from .models import *
from .serializers import destinationsearchSerializer
# from django_filters.rest_framework import DjangoFilterBackend



class DestinationViewSet(viewsets.ModelViewSet):
    queryset = destinstions.objects.all()
    serializer_class = destinationsearchSerializer

    def get_queryset(self):
        queryset= destinstions.objects.all()
       
        search_query = self.request.query_params.get('search',None)
        if search_query:
            queryset=queryset.filter(name_icontains=search_query)

        return queryset






# homepage api
# statically adding data without database
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
            "url": "https://img.freepik.com/free-photo/full-shot-travel-concept-with-landmarks_23-2149153258.jpg?3",
            "img": "https://www.fabhotels.com/blog/wp-content/uploads/2018/08/1400x600-6.jpg",
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
                    "https://karnatakatourism.org/wp-content/uploads/2020/05/Hampi.jpg",
                ],
                "description":" Is a cultural and architectural heritage site built more than 200 years ago. The site was constructed between 1336 AD to 1565 AD. This location is famous for its temples, palaces, market streets and monuments, making up the Vijayanagara Empire.  "
                
            },
            {
                "id": 42,
                "title": "BADAMI",
                "images": [
                    "https://karnatakatourism.org/wp-content/uploads/2020/10/Bhootanatha-Temple-%E2%80%93-Badami.jpg",
                ],
                "description":" It is located in a ravine at the foot of a rugged, red sandstone outcrop that surrounds Agastya lake.  "
            
            },
            {
                "id": 45,
                "title": "MYSORE",
                "images": [
                    "https://karnatakatourism.org/wp-content/uploads/2020/06/mysore-palace-1.jpg",
                    ],
                "description":"  Mysuru has an area of 6,307 sq km and a population of 30,01,127 (2011 census). The city is also known as the City of Palaces, Mysuru has always enchanted its visitors with its quaint charm. "
                
            },
            {
                "id": 43,
                "title": "GOKARNA",
                "images": [
                    "https://www.treebo.com/blog/wp-content/uploads/2018/08/Places-to-See-Near-Gokarna.jpg",
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
    "main_img1": [
       "https://static.toiimg.com/photo/msid-70428261/70428261.jpg",
    
    ],
        "national parks": [
            {
                
                "id": 13,
                "title": "JIM CORBETT NATIONAL PARK",
                "images": [
                    "https://curlytales.com/wp-content/uploads/2022/10/Untitled-design-2022-10-06T184053.043-1170x658.jpg",
                ],
                
            },
            {
                "id": 42,
                "title": "GIR NATIONAL PARK",
                "images": [
                    "https://img.traveltriangle.com/blog/wp-content/uploads/2017/08/Cover13.jpg",
                ],
            
            },
            {
                "id": 4,
                "title": "BENNARGETTA NATIONAL PARK",
                "images": [
                    "https://curlytales.com/wp-content/uploads/2018/07/bnp-4.jpg",
                    ],
                
            },
            {
                "id": 4,
                "title": "PERIYAR NATIONAL PARK",
                "images": [
                    "https://toim.b-cdn.net/pictures/travel_guide/attractions/thmb/periyar-194.jpeg?370x248",
                    ],
                
            }
        ],
     "sub_title2": [
       "TREKING",
    
    ],
        "main_img2": [
            "https://www.shutterstock.com/image-photo/trekking-mountains-mountain-hiking-tourists-260nw-1183637155.jpg"
        ],
        "Treking": [
            {
                
                "id": 13,
                "title": "CHOPTA CHANDRASHILA THUNGNATH",
                "images": [
                    "https://www.trekupindia.com/wp-content/uploads/2022/06/Deoriatalchandrashila-trek-TrekupIndia.jpg",
                ],
                
            },
            {
                "id": 42,
                "title": "CHADAR TREK FROZEN RIVER",
                "images": [
                    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIfVB6Q3oArRKLqXlFBFcUiwBcp_8-ZAr77A&usqp=CAU",
                ],
            
            },
            {
                "id": 4,
                "title": "AUDENS COL EXPEDITION",
                "images": [
                    "https://aquaterra.in/wp-content/uploads/2019/09/Audens-Col-Aquaterra-Main-05.jpg",
                    ],
                
            },
            {
                "id": 4,
                "title": "BINSAR WEEKEND TREK",
                "images": [
                    "https://static.meraevents.com/content/dashboard/tinymce/uploads/binsar-trek-31582880491.jpg",
                    ],
                
            }
        ],
     "sub_title3": [
       "HILLSTATION",
    
    ],
    "main_img3": [
       "https://media.istockphoto.com/id/585282788/photo/view-of-gurtnellen-a-village-in-swiss-alps.jpg?s=612x612&w=0&k=20&c=uWy_ccZ9BVIkfu2JQ_2gWk_FcsXl6XCDIehvvr2En5A=",
    
    ],
        "Hillstations": [
            {
                
                "id": 13,
                "title": " Shimla",
                "images": [
                    "https://media.istockphoto.com/id/1223612773/photo/the-kalka-to-shimla-railway-is-a-2-ft-6-in-narrow-gauge-railway-in-north-india-which.jpg?s=612x612&w=0&k=20&c=vYxFBTbvcLcivcYjtFB-S_P7ETUwgIj0mAk84l9uC1g=",
                ],
                
            },
            {
                "id": 42,
                "title": "Ooty",
                "images": [
                    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmWJu-Q2TAn-H_FvWj7Ye3O2HMD-JVQGmZ9wOsE8dTsUbH-lk0QAOXPDlOzts6s_fKMk8&usqp=CAU",
                ],
            
            },
            {
                "id": 4,
                "title": "Srinagar",
                "images": [
                    "https://www.euttaranchal.com/tourism/photos/srinagar-1946181.jpg",
                    ],
                
            },
            {
                "id": 4,
                "title": " Coorg",
                "images": [
                    "https://media.istockphoto.com/id/1216722235/photo/mountain-with-green-grass-and-beautiful-sky.jpg?s=612x612&w=0&k=20&c=UD4Rmexxtkci9q-gH_PCUaBw6suwTCKp7SkZTXukQ2U=",
                    ],
                
            }
        ],
"sub_title4": [
       "HONEYMOON",
    
    ],
    "main_img4": [
       "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHVG6sSIUksvmDvPHBYH3HulKDzljVc6kwDbuRwyI9exkyuGFhaal3s3uraDnoWjbKWcU&usqp=CAU",
    
    ],
        "Honeymoon": [
            {
                
                "id": 13,
                "title": "GOA",
                "images": [
                    "https://www.holidify.com/images/bgImages/GOA.jpg",
                ],
                
            },
            {
                "id": 42,
                "title": "ANDAMAN",
                "images": [
                    "https://images.travelandleisureasia.com/wp-content/uploads/sites/2/2022/02/09094313/Andaman.jpg",
                ],
            
            },
            {
                "id": 4,
                "title": "HIMACHAL",
                "images": [
                    "https://lp-cms-production.imgix.net/2019-06/GettyImages-149353949_high.jpg",
                    ],
                
            },
            {
                "id": 4,
                "title": "KASHMIR",
                "images": [
                    "https://static.toiimg.com/thumb/msid-96567007,width-748,height-499,resizemode=4,imgsize-184030/.jpg",
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
        "main_img5": [
            "https://upload.wikimedia.org/wikipedia/commons/0/03/Manali_City.jpg",
            
            ],
            "himachal pradesh": [
                {
                    
                    "id": 13,
                    "title": "manali",
                    "images": [
                        "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/05/0f/94/c2/paragliding-in-solang.jpg?w=600&h=400&s=1",
                    ],
                    
                },
                {
                    "id": 42,
                    "title": "Dharamshala",
                    "images": [
                        "https://cdn.onmycanvas.com/wp-content/uploads/2019/09/walkingfromdharamshalabhagsunagvillagemcleodgangarounddharamshalakangravalley.jpeg",
                    ],
                
                },
                {
                    "id": 4,
                    "title": "Dalhousie",
                    "images": [
                        "https://cdn.s3waas.gov.in/s3577bcc914f9e55d5e4e4f82f9f00e7d4/uploads/bfi_thumb/2018041924-olw8nnx2pv9cfxvru4x0p97xxgagosg6fds49z5pca.jpg",
                        ],
                    
                },
                {
                    "id": 4,
                    "title": "Kasol",
                    "images": [
                        "https://images.herzindagi.info/image/2022/Jul/things-to-do-in-kasol-himachal-pradesh_g.jpg",
                        ],
                    
                }
        ],
        "sub_title6": [
            "OOTY",  
        ],
            "main_img6": [
            "https://www.authenticindiatours.com/app/uploads/2022/03/Nilgiri-Hill-Toy-Train-Ooty-Tamil-Nadu-1400x550-c-default.jpg",
            
            ],
            "Ooty": [
                {
                    
                    "id": 13,
                    "title": "Government Rose Garden",
                    "images": [
                        "https://i.ytimg.com/vi/I5UukbPOBZQ/maxresdefault.jpg",
                    ],
                    
                },
                {
                    "id": 42,
                    "title": "Tamilnadu Tourism Ooty Boat House",
                    "images": [
                        "https://www.ttdconline.com/_next/boat-house/ooty/6.jpg"
                    ],
                
                },
                {
                    "id": 4,
                    "title": "Mudumalai Tiger Reserve",
                    "images": [
                        "https://res.cloudinary.com/thrillophilia/image/upload/c_fill,f_auto,fl_progressive.strip_profile,g_auto,q_auto/v1/filestore/zyk5lqym1wik1t6zgopf73xkkqc8_shutterstock_1600599586.jpg",
                        ],
                    
                },
                {
                    "id": 4,
                    "title": "Doddabetta Peak",
                    "images": [
                        "https://www.goldentriangletour.com/userfiles/Doddabeta-DSC_169423.jpg",
                        ],
                    
                }
            ],

     "sub_title7": [
       "MANALI",
    
    ],
        "main_img7": [
             "https://upload.wikimedia.org/wikipedia/commons/0/03/Manali_City.jpg",
        
        ],
            "Manali": [
                {
                    
                    "id": 13,
                    "title": " Hadimba Devi Temple",
                    "images": [
                        "https://i.ytimg.com/vi/CFgEZtnu_-k/maxresdefault.jpg",
                    ],
                    
                },
                {
                    "id": 42,
                    "title": "Old Manali",
                    "images": [
                        "https://media-cdn.tripadvisor.com/media/photo-s/12/ec/12/13/old-manali.jpg",
                    ],
                
                },
                {
                    "id": 4,
                    "title": "Museum of Himachal Culture & Folk Art",
                    "images": [
                        "https://aminus3.s3.amazonaws.com/image/g0023/u00022998/i01221192/9f1a8101f523ce2070a81618f9fe53f3_large.jpg",
                        ],
                    
                },
                {
                    "id": 4,
                    "title": " Rohtang La",
                    "images": [
                        "https://media-cdn.tripadvisor.com/media/photo-s/11/ff/78/6b/800px-cloud-volcano-largejpg.jpg",
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
                    "https://www.nanotraveldiary.com/wp-content/uploads/2021/11/svetski-dan-turizma-2020.jpg"
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
                            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/47/df/c9/the-gopi-island-guesthouse.jpg?w=700&h=-1&s=1"
                        ],

                    },
                    {
                        "id": 50,
                        "title": "Waterfall guest house",
                        "facility": "3 beds,2 bedrooms",
                        "price":"4679/night",
                        "images": [
                            "https://cf.bstatic.com/xdata/images/hotel/max1280x900/77265336.jpg?k=a5927b37f752d71a5b1bf05b369e730fd29b621016b8076183a518d6bad20c6c&o=&hp=1"
                        ],
                    },
                    {
                        "id": 57,
                        "title": "Wild Stone Humpi",
                        "facility": "3beds,2 bedrooms",
                        "price":"4679/night",
                        "images": [
                            "https://cf.bstatic.com/xdata/images/hotel/max1024x768/325565655.jpg?k=68a6d1f553db7a70081ff4d23e4262211f9d1240c69fb52cdfa274450522906f&o=&hp=1"
                        ],
                    },
                    {
                        "id": 59,
                        "title": "Hakuna matata Inn",
                        "facility": "3beds,2 bedrooms",
                        "price":"4679/night",
                        "images": [
                            "https://b.zmtcdn.com/data/pictures/6/59446/cbf6f24316f06181f13919eea8441c81.jpg"
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
                        "https://static.wixstatic.com/media/083278_d4820c98e76c41e2bdea3f10bb7f85c8~mv2.png/v1/fit/w_1000%2Ch_1000%2Cal_c/file.png"
                    ],

                },
                {
                    "id": 6,
                    "title": "Top destinations for food and drink",
                    "images": [
                        "https://www.aworldtotravel.com/wp-content/uploads/2018/10/best-countries-for-food-around-the-world-a-world-to-travel.jpg"
                    ],
                
                },
                
                ],
            
        
  "user": "null"
},
    return Response(data)





