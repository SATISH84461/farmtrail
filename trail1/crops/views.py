from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import create_listing
from datetime import datetime
from .models import categories, crops
from users.models import User
# Create your views here.

def index(request):
    return HttpResponse("Crops")


@login_required(login_url="login")
def create_listings(request):
    if request.method == 'POST':
        data = create_listing(request.POST)
        print(request.POST['crop_name'])
        print(data.is_valid == True)
        if data.is_valid():
            crop_name = request.POST['crop_name']
            crop_desc = request.POST['crop_info']
            crop_quantity = request.POST['crop_quantity']
            crop_image = request.POST['crop_image']
            crop_date = datetime.now()
            crop_cat = request.POST['crop_cat_id']
            crop_cata = ''
            own_name = request.user
            print("Saved")
            for i in categories.objects.all():
                if i.cat_name == crop_cat:
                    pro_cata = i
            final = crops(crop_name=crop_name, crop_info=crop_desc, crop_quantity = crop_quantity,
                                    crop_image=crop_image, crop_date=crop_date, cat_id=pro_cata, owner_name=own_name)
            print("Saved")
            final.save()
            return redirect('index')
    form = create_listing()
    return render(request,"crops/create_listing.html",{
            'create_listing': form,
        })


@login_required(login_url="login")
def my_listing(request):
    name = request.user
    products = crops.objects.filter(owner_name=name)
    return render(request,'crops/my_listings.html',{
        'crops' : products,
        'name': "My Listing",
    })

@login_required(login_url="login")
def crops_details(request,g_id):
    crop_details = crops.objects.filter(id=g_id)[0]
    name = User.objects.filter(id=crop_details.owner_name.id)[0]
    cat = categories.objects.filter(id=crop_details.cat_id.id)[0]
    print(crop_details)
    return render(request, "crops/product_page.html",{
            "crop_details" : crop_details,
            "name": name.username,
            "cat" : cat.cat_name,
            "date" : crop_details.crop_date.date(),
            "g_id" : g_id,
        })
        
@login_required(login_url="login")
def index(request):
    allitems = set(crops.objects.all())
    crop_list = list(allitems)
    def by_date(data):
        return data.crop_date
    crop_list.sort(key=by_date,reverse=True)
    return render(request, "crops/homepage.html",{
        'name' : "Active Listing",
        'crop_list': crop_list,
        'user_name' : request.user,
    })