from ast import Mod
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room,User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','email','password1','password2']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host','roomies']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name','username','email','bio','avatar']