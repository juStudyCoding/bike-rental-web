from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home, name='home'),
    path('signUp',views.signUp, name='signUp'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('mypage',views.mypage, name='mypage'),
    path('reservation',views.reservation, name='reservation'),
    path('weather',views.weather, name='weather'),
    path('location',views.location, name='location'),
    path('notice',views.notice, name='notice'),
    path('board',views.board, name='board'),
    path('contact',views.contact, name='contact'),
    path('notice/<int:pk>/', views.noticeDetail, name='noticeDetail'),
    path('boardWrite', views.boardWrite, name='boardWrite'),
    path('boardEdit/<int:editKey>/', views.boardEdit, name='boardEdit'),
    path('boardDelete/<int:deleteKey>/', views.boardDelete, name='boardDelete'),
    path('reservationDelete/<int:deleteKey>/', views.reservationDelete, name='reservationDelete'),
    ]
urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
