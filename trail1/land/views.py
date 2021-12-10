from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import create_listing
from .models import land
from users.models import User 
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.

def index(request):
    return render(request,"land/index.html")

@login_required(login_url="login")
def create_listings(request):
    if request.method == 'POST':
        data = create_listing(request.POST)
        if data.is_valid():
            area = request.POST['area']
            land_date = datetime.now()
            land_info = request.POST['land_info']
            land_image = request.POST['land_image']
            own_name = request.user
            final = land(land_info=land_info, area = area,
                                    land_image=land_image, land_date=land_date, owner_name=own_name)
            final.save()
            return redirect('index')
    form = create_listing()
    return render(request,"land/create_listing.html",{
            'create_listing': form,
        })


@login_required(login_url="login")
def land_details(request,g_id):
    land_details = land.objects.filter(id=g_id)[0]
    name = User.objects.filter(id=land_details.owner_name.id)[0]
    return render(request, "land/details_page.html",{
            "land_details" : land_details,
            "name": name.username,
            "date" : land_details.land_date.date(),
            "g_id" : g_id,
        })

@login_required(login_url="login")
def index(request):
    allitems = set(land.objects.all())
    land_list = list(allitems)
    def by_date(data):
        return data.land_date
    land_list.sort(key=by_date,reverse=True)
    print(land_list)
    return render(request, "land/index.html",{
        'name' : "Active Listing",
        'land_list': land_list,
        'user_name' : request.user,
    })