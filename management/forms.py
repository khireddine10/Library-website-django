from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
		
class MemoireForm(forms.ModelForm):
    class Meta:
        model = Memoire
        fields = '__all__'



class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrower
        exclude = ['issue_date', 'return_date']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
		
		
class UserRegestration(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model = User # Here when u will create the user
        fields = ['username', 'email', 'password1', 'password2']