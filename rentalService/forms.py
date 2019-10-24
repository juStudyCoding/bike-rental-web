from django import forms
from django.utils import timezone
from .models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        model=Board
        fields = ['title','content']

    def save(self, **kwargs):
        board = super().save(commit=False)
        board.username = kwargs.get('username',None)
        board.updateDate = timezone.now()
        board.save()

