from django.shortcuts import render
from datetime import datetime

 # Django ORM (Object Relational Mapper)

current_tasks = [
    'Create a simple django project',
    'Learn about the various template functions django provides',
    'Learn how to deploy the project'
]

# Create your views here.
def index_page(request):
    return render(request, 'index.html',
                  context={
                      'cur_date': str(datetime.now()),
                      'tasks': current_tasks,
                  })
