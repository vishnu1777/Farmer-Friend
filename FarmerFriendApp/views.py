from django.forms import CharField
from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.db.models import Func, F, Value

from django.views.decorators.csrf import csrf_exempt

from FarmerFriendApp.models import *
import json

from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'user/index.html')

@csrf_exempt
def adminLogin(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        if ((username == "admin") and (password == "admin")):
            return redirect('/home')
        else:
            return redirect('/')

def crops(request):
    data = crop.objects.all().select_related()
    variety_data = variety.objects.all()
    disease_data = disease.objects.all()
    if request.method == 'POST':
        data = crop.objects.filter(crop_name__icontains=request.POST['searchValue']).select_related()
    res = {
        "datas": data,
        "variety_data": variety_data,
        "disease_data": disease_data
    }
    return render(request, 'user/crops.html', res)

def marketing(request):
    data = price.objects.all().select_related()
    crop_data = crop.objects.all()
    res = {
        "datas": data,
        "crop_data": crop_data
    }
    return render(request, 'user/marketing.html', res)

def scheme(request):
    data = schemes.objects.all()
    if request.method == 'POST':
        data = schemes.objects.filter(sc_title__icontains=request.POST['searchValue']).select_related()
    res = {
        "datas": data
    }
    return render(request, 'user/schemes.html', res)

def weatherView(request):
    data = weather.objects.all()
    res = {
        "datas": data
    }
    return render(request, 'user/weather.html', res)

def machinesView(request):
    data = machines.objects.all()
    if request.method == 'POST':
        data = machines.objects.filter(mc_name__icontains=request.POST['searchValue']).select_related()
    res = {
        "datas": data
    }
    return render(request, 'user/machines.html', res)

def videosView(request):
    data = video.objects.all()
    res = {
        "datas": data
    }
    return render(request, 'user/video.html', res)

def newsView(request):
    data = news.objects.all()
    if request.method == 'POST':
        data = news.objects.filter(nw_title__icontains=request.POST['searchValue']).select_related()
    res = {
        "datas": data
    }
    return render(request, 'user/news.html', res)

def addCrop(request):
    crop_type = request.POST["cropType"]
    crop_name = request.POST["cropName"]
    crop_variety = request.POST["cropVariety"]
    crop_disease = request.POST["disease"]
    crop_duration = request.POST["duration"]
    crop_image_url = request.FILES["cropImage"]

    data = crop(crop_type=crop_type, crop_name=crop_name, crop_variety_id=crop_variety, crop_disease_id=crop_disease, crop_duration=crop_duration, crop_image_url=crop_image_url)
    data.save()

    return redirect('/crops/')

def addPrice(request):
    pr_crop_id = request.POST["crop"]
    pr_price = request.POST["cropPrice"]
    pr_updated_datetime = datetime.fromtimestamp(1887639468)

    data = price(pr_crop_id_id=pr_crop_id, pr_price=pr_price, pr_updated_datetime=pr_updated_datetime)
    data.save()

    return redirect('/marketing/')

def addscheme(request):
    sc_id = request.POST["schemeId"]
    sc_title = request.POST["schemeTitle"]
    sc_description = request.POST["schemeDesc"]
    sc_date_time = datetime.fromtimestamp(1887639468)
    sc_img_url = request.FILES["schemeImage"]

    data = schemes(sc_id=sc_id, sc_title=sc_title, sc_description=sc_description, sc_date_time=sc_date_time, sc_img_url=sc_img_url)
    data.save()

    return redirect('/scheme/')

def addWeather(request):
    wt_precipitation = request.POST["precipitation"]
    wt_humidity = request.POST["humidity"]
    wt_wind = request.POST["wind"]
    wt_date = request.POST["date"]

    data = weather(wt_precipitation=wt_precipitation, wt_humidity=wt_humidity, wt_wind=wt_wind, wt_date=wt_date)
    data.save()

    return redirect('/weather/')

def addMachine(request):
    mc_id = request.POST["machineId"]
    mc_name = request.POST["machineName"]
    mc_price = request.POST["machinePrice"]
    mc_contact = request.POST["contact"]
    mc_image_url = request.FILES["machineImage"]

    data = machines(mc_id=mc_id, mc_name=mc_name, mc_price=mc_price, mc_contact=mc_contact, mc_image_url=mc_image_url)
    data.save()

    return redirect('/machines/')

def addVideo(request):
    vd_title = request.POST["videoTitle"]
    vd_thumbnail_url = request.FILES["videoThumbNail"]
    vd_video_url = request.FILES["video"]
    vd_type = request.POST["videoType"]

    data = video(vd_title=vd_title, vd_thumbnail_url=vd_thumbnail_url, vd_video_url=vd_video_url, vd_type=vd_type)
    data.save()

    return redirect('/videos/')

def addNews(request):
    nw_title = request.POST["newsTitle"]
    nw_body = request.POST["newsBody"]
    nw_date_time = datetime.fromtimestamp(1887639468)
    nw_img_url = request.FILES["newsThumbnail"]

    data = news(nw_title=nw_title, nw_body=nw_body, nw_date_time=nw_date_time, nw_img_url=nw_img_url)
    data.save()

    return redirect('/news/')

def deleteCrop(request,id):
    data = crop.objects.get(crop_rid=id)
    data.delete()
    return redirect('/crops/')

def deletePrice(request,id):
    data = price.objects.get(pr_rid=id)
    data.delete()
    return redirect('/marketing/')

def deleteScheme(request,id):
    data = schemes.objects.get(sc_rid=id)
    data.delete()
    return redirect('/scheme/')

def deleteWeather(request,id):
    data = weather.objects.get(wt_rid=id)
    data.delete()
    return redirect('/weather/')

def deleteMachine(request,id):
    data = weather.objects.get(mc_rid=id)
    data.delete()
    return redirect('/machines/')

def deleteVideo(request,id):
    data = video.objects.get(vd_rid=id)
    data.delete()
    return redirect('/videos/')

def deleteNews(request,id):
    data = news.objects.get(nw_rid=id)
    data.delete()
    return redirect('/news/')

def updateCrop(request,id):
    data = crop.objects.get(crop_rid=id)

    data.crop_type = request.POST["cropType"]
    data.crop_name = request.POST["cropName"]
    data.crop_variety_id = request.POST["cropVariety"]
    data.crop_disease_id = request.POST["disease"]
    data.crop_duration = request.POST["duration"]
    data.crop_image_url = request.FILES["cropImage"]
    data.save()

    return redirect('/crops/')

def updatePrice(request,id):
    data = price.objects.get(pr_rid=id)

    data.pr_crop_id_id = request.POST["crop"]
    data.pr_price = request.POST["cropPrice"]
    data.pr_updated_datetime = datetime.fromtimestamp(1887639468)
    data.save()

    return redirect('/marketing/')

def updateScheme(request,id):
    data = schemes.objects.get(sc_rid=id)

    data.sc_id = request.POST["schemeId"]
    data.sc_title = request.POST["schemeTitle"]
    data.sc_description = request.POST["schemeDesc"]
    data.sc_date_time = datetime.fromtimestamp(1887639468)
    data.sc_img_url = request.FILES["schemeImage"]
    data.save()

    return redirect('/crops/')

def updateWeather(request,id):
    data = weather.objects.get(wt_rid=id)

    data.wt_precipitation = request.POST["precipitation"]
    data.wt_humidity = request.POST["humidity"]
    data.wt_wind = request.POST["wind"]
    data.wt_date = request.POST["date"]
    data.save()

    return redirect('/weather/')

def updateMachine(request,id):
    data = machines.objects.get(mc_rid=id)

    data.mc_id = request.POST["machineId"]
    data.mc_name = request.POST["machineName"]
    data.mc_price = request.POST["machinePrice"]
    data.mc_contact = request.POST["contact"]
    data.mc_image_url = request.FILES["machineImage"]
    data.save()

    return redirect('/machines/')

def updateVideo(request,id):
    data = video.objects.get(vd_rid=id)

    data.vd_title = request.POST["videoTitle"]
    data.vd_thumbnail_url = request.FILES["videoThumbNail"]
    data.vd_video_url = request.FILES["video"]
    data.vd_type = request.POST["videoType"]
    data.save()

    return redirect('/videos/')

def updateNews(request,id):
    data = news.objects.get(nw_rid=id)

    data.nw_title = request.POST["newsTitle"]
    data.nw_body = request.POST["newsBody"]
    data.nw_date_time = datetime.fromtimestamp(1887639468)
    data.nw_img_url = request.FILES["newsThumbnail"]
    data.save()

    return redirect('/news/')

def register(request):
    res = {}
    u_name = request.POST["name"]
    u_contact = request.POST["contact"]
    u_password = request.POST["password"]
    u_email = request.POST["email"]
    u_address = request.POST["address"]
    u_pin = request.POST["pin"]

    if not user.objects.filter(u_contact=u_contact).exists():
        data = user(u_name=u_name, u_contact=u_contact, u_password=u_password, u_email=u_email, u_address=u_address, u_pin=u_pin)
        data.save()
        res = {"status": 1, "info": "Success"}
    else:
        res = {"status": -1, "error": "Duplicate Phone Number"}
    
    return HttpResponse(json.dumps(res), content_type="application/json")

def login(request):
    res = {}
    u_contact = request.POST["contact"]
    u_password = request.POST["password"]
    datas = user.objects.filter(
        u_contact=u_contact, u_password=u_password).order_by('u_rid')[:1]

    for data in datas:
        if data.u_contact == u_contact:
            res = {"status": 1, "info": [{"u_rid": data.u_rid,"u_name":data.u_name,"u_contact":data.u_contact,"u_password":data.u_password,"u_email":data.u_email,"u_address":data.u_address,"u_pin": data.u_pin}] }
            return HttpResponse(json.dumps(res), content_type="application/json")

    res = {"status": -1, "error": "Invalid Login Credentials"}
    return HttpResponse(json.dumps(res), content_type="application/json")

def weatherDetails(request):
    data = weather.objects.all().order_by('-wt_rid').values()
    list_disc = list(data)
    res = {"status": 1, "info": list_disc}
    return HttpResponse(json.dumps(res), content_type="application/json")

def newsFeed(request):
    data = news.objects.all().order_by('-nw_rid').values()
    list_disc = list(data)
    res = {"status": 1, "info": list_disc}
    return HttpResponse(json.dumps(res), content_type="application/json")

def priceList(request):
    data = price.objects.all().values('pr_crop_id_id__crop_name','pr_crop_id_id__crop_type','pr_price','pr_updated_datetime')
    list_disc = list(data)
    res = {"status": 1, "info": list_disc}
    return HttpResponse(json.dumps(res), content_type="application/json")

def machineList(request):
    data = machines.objects.all().values()
    list_disc = list(data)
    res = {"status": 1, "info": list_disc}
    return HttpResponse(json.dumps(res), content_type="application/json")

def machineDetails(request):
    mc_rid = request.GET['machineId']
    data = machines.objects.filter(mc_rid=mc_rid).values()
    list_disc = list(data)
    res = {"status": 1, "info": list_disc}
    return HttpResponse(json.dumps(res), content_type="application/json")

def schemeList(request):
    data = schemes.objects.all().order_by('sc_id').values()
    list_disc = list(data)
    res = {"status": 1, "info": list_disc}
    return HttpResponse(json.dumps(res), content_type="application/json")

def cropList(request):
    crop_name = request.GET['cropName']
    data = crop.objects.filter(crop_name__icontains=crop_name).values().order_by('crop_name')
    list_disc = list(data)
    res = {"status": 1, "info": list_disc}
    return HttpResponse(json.dumps(res), content_type="application/json")

def cropDetails(request):
    crop_rid = request.GET['cropId']
    data = crop.objects.filter(crop_rid=crop_rid).values('crop_rid','crop_type','crop_name','crop_variety__vr_name','crop_disease__ds_name','crop_disease__ds_desc','crop_disease__ds_control_methods','crop_duration','crop_image_url')
    list_disc = list(data)
    res = {"status": 1, "info": list_disc}
    return HttpResponse(json.dumps(res), content_type="application/json")

def videoList(request):
    vd_type = request.GET['videoType']
    data = video.objects.filter(vd_type=vd_type).values()
    list_disc = list(data)
    res = {"status": 1, "info": list_disc}
    return HttpResponse(json.dumps(res), content_type="application/json")

def notifications(request):
    data = notification.objects.all().order_by('-not_rid').values()
    list_disc = list(data)
    res = {"status": 1, "info": list_disc}
    return HttpResponse(json.dumps(res), content_type="application/json")

def sellItem(request):
    res = {}
    sell_user_rid = request.POST["farmerRid"]
    sell_crop_rid = request.POST["itemRid"]
    sell_quantity = request.POST["quantity"]
    sell_unit_price = request.POST["price"]
    sell_desc = request.POST["desc"]
    sell_total_price = request.POST["totalCost"]
    sell_date = datetime.fromtimestamp(1887639468)

    data = sell(sell_user_rid_id=sell_user_rid, sell_crop_rid_id=sell_crop_rid, sell_quantity=sell_quantity, sell_unit_price=sell_unit_price, sell_desc=sell_desc, sell_total_price=sell_total_price, sell_date=sell_date)
    data.save()
    res = {"status": 1, "info": "Success"}
    
    return HttpResponse(json.dumps(res), content_type="application/json")

def buyItemList(request):
    sell_user_rid = request.GET['farmerRid']
    data = sell.objects.filter(sell_quantity__gt=0).exclude(sell_user_rid_id=sell_user_rid).values(
        'sell_rid','sell_user_rid_id','sell_crop_rid','sell_crop_rid__crop_name','sell_crop_rid__crop_image_url','sell_quantity','sell_unit_price','sell_total_price', 'sell_date', 'sell_desc'
    )
    list_disc = list(data)
    res = {"status": 1, "info": list_disc}
    return HttpResponse(json.dumps(res), content_type="application/json")

def buyItem(request):
    res = {}
    buy_user_rid = request.POST["buyerRid"]
    buy_sell_rid = request.POST["sellRid"]
    buy_qty = request.POST["quantity"]
    buy_date = datetime.fromtimestamp(1887639468)

    data = buy(buy_user_rid_id=buy_user_rid, buy_sell_rid_id=buy_sell_rid, buy_qty=buy_qty, buy_date=buy_date)
    data.save()

    item = sell.objects.get(sell_rid=buy_sell_rid)
    item.sell_quantity -= float(buy_qty)
    item.save()

    res = {"status": 1, "info": "Success"}
    return HttpResponse(json.dumps(res), content_type="application/json")

def orderList(request):
    farmer = request.GET['farmerRid']
    data = buy.objects.filter(buy_sell_rid__sell_user_rid_id=farmer).values(
        'buy_qty', 'buy_date', 'buy_sell_rid__sell_crop_rid__crop_name', 'buy_sell_rid__sell_user_rid__u_name'
    ).order_by('-buy_rid')
    list_disc = list(data)
    res = {"status": 1, "info": list_disc}
    return HttpResponse(json.dumps(res), content_type="application/json")
