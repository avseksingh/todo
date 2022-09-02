from django.contrib import admin
from django.urls import path, include
from todo.views import todo_list
from todo.views import addTodoView
from todo.views import deleteTodoView
urlpatterns = [
    path('admin/', admin.site.urls),
]