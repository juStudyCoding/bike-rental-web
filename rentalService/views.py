from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Notice, Board, Reservation
from .weather_api import get_weather_data
from .forms import BoardForm
from django.utils import timezone
import logging
#from django.core.urlresolvers import reverse

# Create your views here.
def home(request):
    return render(request, 'rentalService/home.html',{})

def signUp(request):
    if request.method=="POST":
        #if form.is_valid():
        #message = form.cleaned_data['message']
        if request.POST["password"] == request.POST["passwdCheck"]:

            user = User.objects.create_user(
                username= request.POST["username"],
                password= request.POST["password"],
                email = request.POST["email"]
            )
            auth.login(request,user)
            request.session["username"]=username
            return render(request, 'rentalService/home.html',{})
        return render(request, 'rentalService/signUp.html')
    else:
        return render(request, 'rentalService/signUp.html',{})

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:

            auth.login(request,user)
            request.session["username"]=username
            #return render(request, 'rentalService/home.html', {'loginCheck':'T',})
            return redirect('home')
        else:
            return render(request, 'rentalService/login.html',{'error':'username or password is incorrect'})
    else:
        return render(request, 'rentalService/login.html')

def logout(request):
    #if request.method=="POST":
        auth.logout(request)
        request.session.flush()
        return redirect('home')

def reservation(request):
    if request.method== "POST":
        reservation=Reservation()
        reservation.username=User.objects.get(username=request.user.get_username())
        reservation.sort = request.POST["sort"]
        reservation.quantity = request.POST["quantity"]
        reservation.start_date = request.POST["start_date"]
        reservation.end_date = request.POST["end_date"]
        reservation.total = request.POST["total"]
        reservation.createTime = timezone.now()
        reservation.save()
        return render(request, 'rentalService/reservCompleted.html',)
    else:
        if request.session.get("username",False):
            return render(request, 'rentalService/reservation.html',)
        else:
            return render(request, 'rentalService/login.html',{'error':'로그인 후 이용가능합니다.'})

def notice(request):
    noticeList = Notice.objects.all()
    return render(request, 'rentalService/notice.html', {'noticeList':noticeList})

def noticeDetail(request, pk):
    notice = Notice.objects.get(pk=pk)
    return render(request, 'rentalService/noticeDetail.html',{'notice':notice})

def mypage(request):
    reservList=Reservation.objects.filter(username= request.user)
    nums = Reservation.objects.count()
    return render(request, 'rentalService/mypage.html', {'reservList':reservList, 'nums':nums})

def reservationDelete(request, deleteKey):
    reservation = Reservation.objects.get(pk=deleteKey)
    reservation.delete()
    return redirect('mypage')


def weather(request):
    weatherData = {}
    weatherData = get_weather_data()
    return render(request, 'rentalService/weather.html',{'weatherData':weatherData})

def location(request):
    return redirect('home')

def board(request):
    boardList = Board.objects.all()
    nums = Board.objects.count()
    return render(request, 'rentalService/board.html', {'boardList':boardList, 'nums':nums})
def boardWrite(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save(username = request.user)
        return  redirect('board')
    else:
        form = BoardForm()
        return render(request, 'rentalService/boardWrite.html',{'form':form})
    return redirect('home')

def boardEdit(request, editKey):
    if request.method =="POST":
        board = Board.objects.get(pk = editKey)
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save(username = request.user)
            return redirect('board')
    else:
        board=Board.objects.get(pk = editKey)
        if board.username == User.objects.get(username = request.user.get_username()):
            form = BoardForm(instance = board)
            check = "edit"
            return render(request,'rentalService/boardWrite.html' ,{'board':board, 'form':form, 'check':check} )
        else:
            return render(request, 'rentalService/error.html')

def boardDelete(request, deleteKey):
    board = Board.objects.get(pk=editKey)
    if board.username == User.objects.get(username = request.user.get_username()):
        board.delete()
        return redirect('board')
    else:
        return render(request, 'rentalService/error.html')


def contact(request):
    return render(request, 'rentalService/contact.html',{})
