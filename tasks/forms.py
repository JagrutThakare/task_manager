from django import forms
from tasks.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'deadline', 'status', 'description']
        widgets = {
            'title' : forms.TextInput( attrs={'class':'form-control'}),
            'deadline' : forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'status' : forms.Select(attrs={'class': 'form-select'}),
            'description' : forms.TextInput(attrs={'class':'form-control'}),
        } 

