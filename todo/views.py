from django.shortcuts import render
from .models import User
# Create your views here.


def get_todo_list(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'todo/todo_list.html', context)


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('register_user')
        password = 
    return render(request, 'todo/register.html')
