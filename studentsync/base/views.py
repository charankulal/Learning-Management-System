from django.shortcuts import render
from .models import Room


def home(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request,'base/home.html',context)


def room(request,pk):
    rooms=Room.objects.get(id=pk)
    context={'rooms':rooms}
            
    return render(request,'base/room.html',context)

def createRoom(request):
    context={}
    return render(request,'base/room_form.html',context)
