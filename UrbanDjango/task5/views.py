from django.template.response import TemplateResponse
from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from django import forms


user_list = ['user1', 'user2']
info = {}
def condition(username, password, repeat_pass, age):
    if username in user_list:
        info['error'] = 'Пользователь уже существует'
        return info
    if password != repeat_pass:
        info['error'] = 'Пароли не совпадают'
        return info
    if age < 18:
        info['error'] = 'Вы должны быть старше 18'
        return info
    else:
        info['username'] = username
        info['password'] = password
        info['age'] = age
        return info

def sign_up_by_html(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_pass = request.POST.get('repeat_pass')
        age = request.POST.get('age')

        info = condition(username, password, repeat_pass, int(age))

        return render(request, 'fifth_task/registration_page.html', context=info)
    return render(request, 'fifth_task/registration_page.html')

def sign_up_by_django(request):
    info = {'form': RegistrationForm()}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            repeat_pass = form.cleaned_data.get('repeat_pass')
            age = form.cleaned_data.get('age')
            info_1 = condition(username, password, repeat_pass, age)
            context = info|info_1
        return render(request, 'fifth_task/registration_page_django.html', context=context)

    return render(request, 'fifth_task/registration_page_django.html', context=info)


