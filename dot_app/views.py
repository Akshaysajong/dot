from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import update_session_auth_hash
from .form import RegisterForm,EntrollmentForm
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
            # groups = form.cleaned_data.get('groups')
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
    # if request.user.is_authenticated:
    # u= User.objects.filter(is_superuser = '0')
        # v= request.user.is_authenticated
        user = request.user
        # userquery = User.objects.all()
        # user_group = ''
        # for x in userquery :
        #     userid= x.id
        #     print(x.groups)
        #     print('########################################################')
        #     group_name=user.groups.all().filter(user=userid)
        #     print(group_name)
        #     user_group = group_name[0].name  
        #     print(user_group)
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
    print(ctry)
    st=state.objects.all()
    cty=city.objects.all()
    return render(request,'addhotels.html',{'country':ctry,'states':st,'city':cty})


# def admin_viewhotels(request):
#     a= hotels.objects.all()
#     return render(request, "admin/js_view.html",{'b':a})


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



@login_required(login_url="/login")
def ajax_state(request):
    s_id = request.GET['state']
    cit = city.objects.all().filter(state_id=s_id)
    dat = []
    for x in cit:
        dat.append({'name':x.name, 'id':x.id})
        print(dat)
    return JsonResponse(dat, safe=False)


@login_required(login_url="/login")
def dot_destination_area(request):
    return render(request, "destinationarea.html")

@login_required(login_url="/login")
def dot_add_destination_area(request):
    if request.method == 'POST':
        destn_area = request.POST['destn_area']
        place = request.POST['place']
        statu = request.POST['status']
        d_area = destination_area(name=destn_area, place=place, status=statu)
        d_area.save()
    return redirect("dot_destination_area")


def dot_edit_destination(request):
    pass
@login_required(login_url="/login")
def dot_view_destinationarea(request):
    destn_area = destination_area.objects.all()
    return render(request, "view_destinationarea.html",{'destn_area':destn_area})

@login_required(login_url="/login")
def dot_destinations(request):
    destn_area = destination_area.objects.all()
    return render(request, "add_destinations.html",{'destn_area':destn_area})

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
        dstn = destinstions(name=destn, d_area_id=destn_area, address=address, description=description, climate=climate, culture=culture)
        dstn.save()
        for x in img:
            b=destination_img(destinstions_id=dstn.id, image=x)
            # b= PostImage(places_idd_id=a.id,images=img)
            b.save()
    return redirect("dot_destinations")

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


