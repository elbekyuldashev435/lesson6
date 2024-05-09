from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUser
from .forms import CustomUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.


""" first way to add data to db """
# class RegisterView(View):
#     def get(self, request):
#         return render(request, 'register.html')
#
#     def post(self, request):
#         username = request.POST['username']
#         password = request.POST['password']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#
#         user = CustomUser.objects.create_user(
#             username=username,
#             first_name=first_name,
#             last_name=last_name,
#             email=email
#         )
#         user.set_password(password)
#         user.save()
#
#         return redirect('users:login')


class RegisterView(View):
    def get(self, request):
        create_form = CustomUserForm()
        context = {
            'form': create_form
        }
        return render(request, 'register.html', context=context)

    def post(self, request):
        create_form = CustomUserForm(data=request.POST, files=request.FILES)
        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')
        else:
            context = {
                'form': create_form
            }
            return render(request, 'register.html', context=context)


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {
            'form': login_form
        }
        return render(request, 'login.html', context=context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home:landing_page')
        else:
            context = {
                'form': login_form
            }
        return render(request, 'login.html', context=context)