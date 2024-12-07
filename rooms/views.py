from django.shortcuts import render, redirect
from rooms.models import Room

def index(request):
    return render(request,'index.html')

def admin(request):
    return render

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def gallery(request):
    return render(request,'gallery.html')

def room(request):
    return render(request,'room.html')

 # def home(request):
    # return render(request,'home.html')
    

def viewdata(request):
    return render(request, 'viewdata.html')



def book_now(request):
    if request.method != 'POST':
        return render(request,'book.html')
    name=request.POST['name']
    email=request.POST['email']
    arrival=request.POST['arrival']
    departure=request.POST['departure']
    phone_number=request.POST['phone_number']
    guests=request.POST[guests]

    rooms = Room(arrival=arrival, departure=departure, phone_number=phone_number, name=name, email=email, guests=guests)
    room.save()
    return redirect('index.html')


