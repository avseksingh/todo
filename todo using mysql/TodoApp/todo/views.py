from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from todo.models import TodoItem
from .forms import TodoForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def loginView(request):
    if request.method == 'GET':
	    form1 = AuthenticationForm()
	    context = {
    		"form": form1
    	}
	    return render(request, "login.html", context)
    else:
        form = AuthenticationForm(data=request.POST)
        welcome_user= request.POST['username']
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/todolist")
        else:
            context = {
                "form" : form
            }
            return render(request , 'login.html' , context=context )

def signupView(request):
	if request.method == 'GET':
		form = UserCreationForm()
		context={
			"form": form
		}
		return render(request, "signup.html", context)
	else:
		form=UserCreationForm(request.POST)
		context={
				"form": form
			}
		if form.is_valid():
			is_created=form.save()
			if is_created:
				print("created")
				return HttpResponseRedirect("/login")
		else:
			return render(request, "signup.html", context)
		 
@login_required(login_url='login')
def todo_list(request):
	all_todo_items = TodoItem.objects.all()
	user=request.user.username
	context={
        'alltodoitems': all_todo_items,
		'user': user
    }
	return render(request, "index.html", context)

@login_required(login_url='login')
def addTodoView(request):
	if request.method == 'POST':
		 posttitle = request.POST['title']
		 new_item = TodoItem(title=posttitle)
		 new_item.save()
		 return HttpResponseRedirect('/')
	return HttpResponseRedirect('/')

@login_required(login_url='login')
def updateTodoView(request, pk=0):
	task = TodoItem.objects.get(id=pk)
	if request.method == 'POST':
		form = TodoForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/') 

	form = TodoForm(instance=task)
	context = {'form':form}
	return render(request, 'update.html', context)

@login_required(login_url='login')
def completeTodoView(request, pk):
	TodoItem.objects.filter(id=pk).update(is_completed=True)
	return HttpResponseRedirect('/')
	
@login_required(login_url='login')
def undoneView(request, pk):
	TodoItem.objects.filter(id=pk).update(is_completed=False)
	return HttpResponseRedirect('/')

@login_required(login_url='login')       
def deleteTodoView(request, pk):
	item = TodoItem.objects.get(id=pk)
	item.delete()
	return HttpResponseRedirect('/')

@login_required(login_url='login')
def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/')
