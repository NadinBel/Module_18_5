from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(widget=forms.PasswordInput(), label='Введите пароль')
    repeat_pass = forms.CharField(widget=forms.PasswordInput(), label='Повторите пароль')
    age = forms.IntegerField(label='Введите свой возраст')