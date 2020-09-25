from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from tasks.models import Tag, Task
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            # send email
            return redirect('tasks')
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})


@login_required(login_url='login')
def dashboard(request):
    user = request.user
    tasks = user.task_set.all()
    tags = user.tag_set.all()
    return render(request, 'pages/dashboard.html', {'tasks': tasks, 'tags': tags})
