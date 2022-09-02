from django import forms
from todo.models import TodoItem
 
class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields="__all__"
    