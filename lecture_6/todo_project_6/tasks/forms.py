from django import forms

from tasks.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'deadline', 'tags']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
