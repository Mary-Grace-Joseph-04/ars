from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import auth

from arsapp.forms import UserRegisterForm, reservedetailsform

from django.contrib import messages
from .models import reservedetails, places, classes

# Create your views here.
def index(request):
    return render(request,'index.html')
    
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print('Registered Successfully')
            try:
                form.save()
                messages.success(request,'Account is created')
                return redirect('index')
            except:
                print('Error Occur')
                pass

    else:
        print('Something  wrong happened ')
        form = UserRegisterForm()

    return render(request,'register.html',{'form':form})
    

def Login(request):
    

    # if request.method =='POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(username = username, password = password)
    #     if user is not None:
    #         if user.is_staff == True:
    #             return redirect('ownerhome')
    #         else:
    #             form = auth_login(request,user)
    #             messages.success(request,f'welcome {username} !!')
    #             return redirect('userhome') 
    #     else:
    #         messages.info(request,'account done not exit plz sign in')

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_staff == True:
                return redirect('ownerhome')
            else:
                form =login(request,user)
                messages.success(request,f'welcome {username} !!')
                return redirect('userhome')
        else:
            messages.info(request, 'invalid username and password')
            return redirect('login_url')
       
    else:
        return render(request,'Login.html') 
        


def ownerhome(request):
    return render(request,'ownerhome.html')

def userhome(request):
    return render(request,'userhome.html')

def reservation(request):
    form =reservedetailsform()
    if request.method == 'POST':
        form =reservedetailsform(request.POST)
        if form.is_valid:
            try:
                thought = form.save(commit=False)
                thought.user = request.user
                form.save()
                messages.success(request,'Your flight ticket is booked successfully')
                return redirect('userhome')
            except:
                print("hehhhhhh")
    else:
        form1 = reservedetailsform()
    return render(request,'reservation.html',{'form':form})  

def logout(request):
    auth.logout(request)
    return redirect('login')


def reservation_list(request):
    reservation = reservedetails.objects.filter(user=request.user)
    context = {'reservation':reservation,}
    return render(request, 'view-details.html', context)



def reservation_edit(request, id):
    reservation = reservedetails.objects.get(pk=id)
    place = places.objects.all()
    classe = classes.objects.all()
    context = {
        'reservation': reservation,
        'places': place,
        'classes': classe,
    }
    if request.method == 'GET':
        return render(request, 'edit-reservation.html', context)
    if request.method == 'POST':
        departure_city = request.POST['departure_city']
        arrival_city = request.POST['arrival_city']
        date = request.POST['date']
        Class = request.POST['classes']
        # today = date.today() 

        if departure_city == arrival_city:
             messages.error(request, 'Both arrival and destination is same')
             return render(request, 'edit-reservation.html', context)

        # if date < today:
        #      messages.error(request, 'enter a valid date')
        #      return render(request, 'edit-reservation.html', context)

        reservation.departure_city = departure_city
        reservation.arrival_city = arrival_city
        reservation.date = date
        reservation.Class = Class

        reservation.save()
        # messages.success(request, 'Record updated  successfully')

        return redirect('view-details')

def cancel_list(request):
    reservation = reservedetails.objects.filter(user=request.user)
    context = {'reservation':reservation,}
    return render(request, 'cancel-list.html', context)

def cancel_reservation(request, id):
    reservation = reservedetails.objects.get(pk=id)
    reservation.delete()
    # messages.success(request, 'record removed')
    return redirect('cancel_list_url')
 