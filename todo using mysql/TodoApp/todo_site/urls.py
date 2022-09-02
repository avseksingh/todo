from django.contrib import admin
from django.urls import path, include
from todo.views import todo_list
from todo.views import addTodoView
from todo.views import deleteTodoView
from todo.views import updateTodoView
from todo.views import completeTodoView
from todo.views import loginView
from todo.views import signupView
from todo.views import todo_list
from todo.views import undoneView
from todo.views import logoutView

urlpatterns = [
    path('', todo_list),
    path('admin/', admin.site.urls),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('signup/', signupView),
    path('addTodoItem/', addTodoView), 
    path('todolist/', todo_list), 
    path('deleteTodoItem/<str:pk>/', deleteTodoView, name="delete"), 
    path('updateTodoItem/<str:pk>/', updateTodoView, name="update"),
    path('completeTodoItem/<str:pk>/', completeTodoView, name="complete"),
    path('undone/<str:pk>/', undoneView, name="undone"),
]
