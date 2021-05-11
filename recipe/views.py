from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from recipe.models import Recipe

def user_login(request):

    return render(request,'recipe/login.html')

def register(request):
    return render(request,'recipe/register.html')

def login_success_or_not(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/recipe/show/')
    else:
        return HttpResponse("<html><body bgcolor='red'><h1>'Invalid username or password '<h1></body></html>")

def save_details(request):
    user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'],email=request.POST['email'])
    return HttpResponseRedirect('/recipe/')

def show(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/show.html', {'recipe': recipes})

def details(request,recipe_id):
    user=User.objects.all()
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request,'recipe/details.html',{'recipe':recipe,'user':user})

def save_recipe(request):
    Recipe.objects.create(recipe_name=request.POST["name"],ingredients=request.POST["ingredients"],
                          process=request.POST["process"],pub_date=timezone.now(),image=request.FILES['image'])
    return HttpResponseRedirect("/recipe/show/")

def create_page(request):
    return render(request,"recipe/create_page.html")

def delete_recipe(request, recipe_id):
    Recipe.objects.get(pk=recipe_id).delete()
    return HttpResponseRedirect("/recipe/show/")

def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/recipe/")
