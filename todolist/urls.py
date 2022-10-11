from django.urls import path
from todolist.views import (delete, add_task, delete_task, show_json, delete_task, show_todolist, register, login_user, logout_user, create_task, invert_task_status, delete_task)

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('add/', add_task, name='add-task'),
    path('invert-task-status/<int:task_id>/', invert_task_status, name='invert-task-status'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('delete/<int:task_id>/', delete, name='delete'),
    path('json/', show_json, name='json'),
]