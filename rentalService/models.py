from django.db import models
from django.contrib.auth.models import User
import logging
# manage.py makemigrations rentalService
# manage.py migrate  model변경되면 이 두줄 실행


# Create your models here.
class Reservation(models.Model):
    username=models.ForeignKey(User, on_delete = models.CASCADE)
    sort = models.CharField(max_length=30)
    quantity = models.IntegerField()
    start_date=models.DateField(blank=False,)
    end_date = models.DateField(blank=False,)
    total=models.CharField(max_length=30)
    createTime = models.DateTimeField(auto_now_add=True)
    #https://devdoggo.netlify.com/post/python/django/counter/
    def clean(self, *args, **kwargs):
        super().clean(*args, **kwargs)
    def save(self, *args, **kwargs):
        self.full_clean() #to handle validation
        super(Reservation,self).save()


#https://wayhome25.github.io/django/2017/03/01/django-99-my-first-project-4/
#위 주소 참조하기(방명록)

class Notice(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    creatTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    photo = models.ImageField(blank=True, null = True)
    class Meta:
        ordering = ['-updateTime']
    def __str__(self):
        return self.title

class Board(models.Model):
    username = models.ForeignKey(User, on_delete = models.CASCADE )
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=150, help_text='메모 내용은 150자 이내로 입력 가능합니다.')
    updateDate =  models.DateTimeField()
