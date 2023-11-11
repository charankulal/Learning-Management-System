from django.shortcuts import render
from .models import Room

# rooms=[
#     {'id':1,'name':'Lets learn Python'},
#     {'id':2,'name':'Design with me'},
#     {'id':3,'name':'Front end Developers Club'},
# ]

def home(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request,'base/home.html',context)


def room(request,pk):
    rooms=Room.objects.get(id=pk)
    context={'rooms':rooms}
            
    return render(request,'base/room.html',context)
