from django import forms

from tasks.models import Task


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(max_length=65536, widget=forms.Textarea)
    sender = forms.EmailField()


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'deadline', 'tags']
        widgets = {
            'deadline': forms.DateTimeInput(attrs = {'type': 'datetime-local'})
        }
