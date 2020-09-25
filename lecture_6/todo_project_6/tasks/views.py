from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import TaskForm, TagForm


@login_required(login_url='login')
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        form.instance.user = request.user
        if form.is_valid():
            task = form.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})


@login_required(login_url='login')
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(data=request.POST)
        form.instance.user = request.user
        if form.is_valid():
            tag = form.save()
            return redirect('dashboard')
    else:
        form = TagForm()
    return render(request, 'tasks/add_tag.html', {'form': form})
