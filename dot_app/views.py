from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import update_session_auth_hash
from .form import RegisterForm,AddHotelsForm
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password


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
    ctry=country.objects.all()
    st=state.objects.all()
    cty=city.objects.all()
    org=organization.objects.all()
    return render(request,'addhotels.html',{'country':ctry,'states':st,'city':cty,'organization':org})

# add hotels
def dot_addhoteldb(request):
    if request.method == "POST":
        hoteltype = request.POST['hoteltype']
        contact_person = request.POST['contact_person']
        phone= request.POST['phone']
        user_name = request.POST['user_name']
        pwd = request.POST['pwd']
        address = request.POST['address']
        cotry_id = request.POST['country'] 
        sts_id = request.POST['state']
        citi_id = request.POST['city']
        organtn_id = request.POST['organization']
        cnty = country.objects.all().filter(id=cotry_id)
        sts = state.objects.all().filter(id=sts_id)
        citi = city.objects.all().filter(id=citi_id)
        password = 'PASSWORD_HERE'
        form = AddHotelsForm
        if request.method == "POST":
         form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            print(username)
        # if form.is_valid():
        #     user = form.save()
        form.password = make_password(password)
        # form.save()
        ho = User(username=user_name, password=pwd)
        ho.save()
        print(ho.id) 
        gr_id = request.POST.getlist('groups')
        # idd= gr_id[0]
        print(gr_id)
        for x in  gr_id:
                print(x)
                # user.groups.add(x)
        hotl = userprofile(user_id=ho.id, organization_id=organtn_id, hotel_type=hoteltype, contact_person=contact_person, phone=phone, address=address, country=cnty[0].name, state=sts[0].name, city=citi[0].name)
        hotl.save()

    return redirect('dot_addhotel')

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

#delete hotel
@login_required(login_url="/login")
def delete_hotel(request):
    d_id = request.GET['d_id']
    htl = userprofile.objects.all().filter(id=d_id).delete()
    dat = ['hotel deleted']
    return JsonResponse(dat, safe=False)

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
        destn_area = request.POST['destn_area']
        place = request.POST['place']
        statu = request.POST['status']
        cuntry_id = request.POST['country']
        state_id = request.POST['state']
        coutry = country.objects.all().filter(id = cuntry_id)
        stat = state.objects.all().filter(id = state_id)
        lattitude = request.POST['lattitude']
        longitude = request.POST['longitude']
        d_area = destination_area(name=destn_area, place=place, status=statu, country=coutry[0].name, state=stat[0].name, lattitude=lattitude, longitude=longitude)
        d_area.save()
    return redirect("dot_destination_area")

#edit destination area
@login_required(login_url="/login")
def dot_edit_destinationarea(request):
    ed_id = request.GET['a']
    destn = destination_area.objects.all().filter(id=ed_id)
    return render(request, "edit_destinationarea.html",{'destn':destn})

#delete destination area
@login_required(login_url="/login")
def delete_darea(request):
    d_id = request.GET['d_id']
    destn = destination_area.objects.all().filter(id=d_id).delete()
    dat = ['Destination area deleted']
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
        destn = request.POST['destn']
        destn_area = request.POST['destn_area']
        print(destn_area)
        img = request.FILES.getlist('image')
        address = request.POST['address']
        description = request.POST['description']
        climate = request.POST['climate']
        culture = request.POST['culture']
        lattitude = request.POST['lattitude']
        longitude = request.POST['culture']
        dstn = destinstions(name=destn, d_area_id=destn_area, address=address, description=description, climate=climate, culture=culture, longitude=longitude, lattitude=lattitude)
        dstn.save()
        for x in img:
            b=destination_img(destinstions_id=dstn.id, image=x)
            b.save()
    return redirect("dot_destinations")

#view destination list
@login_required(login_url="/login")
def dot_view_destination(request):
    destn = destinstions.objects.all()
    print(destn)
    destn_list=[]
    #c = PostImage.objects.all()
    for x in destn:
        print('#################################################')
        # print(x.place_name)
        print(x.id)
        img= destination_img.objects.all().filter(destinstions=x.id)
        # print('>>>>>>>>>>>>>>')
        # print(img[0].id)
        im =''
        if img:
            im = img[0].image
        destn_list.append({'id':x.id, 'name':x.name,'address':x.address , 'description':x.description,'climate':x.climate,'culture':x.culture, 'image':im})
    return render(request, "view_destination.html",{'destn_list':destn_list})

def dot_editdestination(request):
    e_id = request.GET['a']
    print(e_id)
    destn = destinstions.objects.all().filter(id=e_id)
    return render(request, 'edit_destination.html', {'destn':destn})


@login_required(login_url="/login")
def dot_content(request):
    ctnt=content.objects.all()
    print(ctnt)
    return render(request,'content.html',{'content':ctnt})