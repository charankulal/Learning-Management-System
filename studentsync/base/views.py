from django.shortcuts import render,redirect
from .models import Room
from .forms import RoomForm

def home(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request,'base/home.html',context)


def room(request,pk):
    rooms=Room.objects.get(id=pk)
    context={'rooms':rooms}
            
    return render(request,'base/room.html',context)

def createRoom(request):
    form=RoomForm
    if request.method=="POST":
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/room_form.html',context)
