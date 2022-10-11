import datetime
from django.shortcuts import (render, redirect)
from django.http import (Http404, HttpResponseRedirect, HttpResponse)
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.utils import timezone
from todolist.models import Task
from project_django.settings import DOMAIN


@login_required(login_url='/todolist/login')
def show_todolist(request):
  return render(request, "todolist.html", 
    {
      "tasks": Task.objects.filter(user=request.user),
      "last_update": request.COOKIES.get("last_update", None),
      "domain": DOMAIN,
    }
  )


@login_required(login_url='/todolist/login')
def create_task(request):
  if request.method == "POST":
    title = request.POST.get("title")
    description = request.POST.get("description")
    Task.objects.create(title=title, description=description, user=request.user)
    response = HttpResponseRedirect(reverse('todolist:show_todolist'))
    response.set_cookie('last_update', timezone.now())
    return response
  
  return render(request, "create_task.html", {})


def delete(request, task_id):
  if request.method == "DELETE":
    task = Task.objects.get(id = task_id)
    task.delete()
    return redirect('todolist:show_todolist')
  raise Http404("Request method invalid")

def delete_task(request, task_id):
  task = Task.objects.get(id = task_id)
  task.delete()
  return redirect('todolist:show_todolist')


def invert_task_status(request, task_id):
  task = Task.objects.get(id = task_id)
  task.is_finished = not task.is_finished
  task.save()
  return redirect("todolist:show_todolist")


def register(request):
  form = UserCreationForm()

  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Akun telah berhasil dibuat!')
      return redirect('todolist:login')
    
  context = { 'form' : form }
  return render(request, 'register.html', context)


def login_user(request):
  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      response = HttpResponseRedirect(reverse('todolist:show_todolist'))
      response.set_cookie('last_login', str(datetime.datetime.now()))
      return response
    else:
      messages.info(request, "Username atau Password salah!")
  return render(request, 'login.html', {})


def logout_user(request):
  logout(request)
  response = HttpResponseRedirect(reverse('todolist:login'))
  response.delete_cookie('last_login')
  return response


def show_json(request):
  return HttpResponse(
    serializers.serialize("json", Task.objects.all()),
    content_type="application/json"
  )
  
  
@login_required(login_url='/todolist/login')
def add_task(request):
  if request.method == "POST":
    title = request.POST.get("title")
    description = request.POST.get("description")
    Task.objects.create(title=title, description=description, user=request.user)
    response = HttpResponseRedirect(reverse('todolist:show_todolist'))
    response.set_cookie('last_update', timezone.now())
    return response
  
  raise Http404("Invalid request method")
