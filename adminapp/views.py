from django.shortcuts import render,redirect
from adminapp.models import AdminLoginModel,RoomModel
from customerapp.models import RoomBookingModel
from django.contrib import messages
from datetime import datetime
from django.shortcuts import get_object_or_404
# Create your views here.
def showindex(request):
    return render(request,"adminn/login.html")
def admin_login_check(request):
    admin_name = request.POST.get("admin")
    password = request.POST.get("pswrd")
    if  admin_name=='sowmya' and password=='sowmya':
        return render(request, 'adminn/admin_index.html')
    else:
        print("error")
        return render(request, "adminn/login.html", {"error": "Invalid Admin"})
def welcome(request):
    return render(request,'adminn/admin_index.html')
def admin_logout(request):
    return render(request ,'adminn/login.html')
def admin_add_rooms(request):
    return render(request, "adminn/admin_add_rooms.html")
def admin_save_room(request):
    room_type=request.POST.get("a1")
    room_Capacity=request.POST.get("a2")
    room_image = request.FILES["a3"]
    datee=request.POST.get("a4")
    print(datetime)
    RoomModel(type=room_type,capacity=room_Capacity,image=room_image,add_date=datee,status="available").save()
    messages.success(request,"added sucessfully")
    return render(request, 'adminn/admin_add_rooms.html')


def admin_edit_rooms(request):
    data=RoomModel.objects.all()
    return render(request, 'adminn/admin_edit_rooms.html', {"data":data})

def editing_process(request):
    cid=request.GET.get("cid")
    res=RoomModel.objects.filter(id=cid)
    return render(request, "adminn/editing_process.html", {"data":res})

def admin_reports(request):
    res=RoomBookingModel.objects.all()
    print(res)
    return render(request, 'adminn/admin_reports.html', {"data":res})


def admin_search(request):
    fd=request.POST.get("d1")
    td=request.POST.get("d2")
    res=RoomBookingModel.objects.filter(checkin__range=(fd,td))
    return render(request, 'adminn/admin_reports.html', {"data": res})


def admin_delete_room(request):
    rid=request.GET.get("rid")
    RoomModel.objects.get(id=rid).delete()
    return admin_edit_rooms(request)


def admin_update_edit(request):

    idno=request.POST.get("a5")
    roomid=get_object_or_404(RoomModel,id=idno)
    roomid.type = request.POST.get("a1")
    roomid.capacity = request.POST.get("a2")
    roomid.image = request.FILES["a3"]
    roomid.date = request.POST.get("a4")
    roomid.save()
    # RoomModel.objects.filter(id=idno).update(type=type,capacity=capacity,image=image,add_date=date)
    return admin_edit_rooms(request)

