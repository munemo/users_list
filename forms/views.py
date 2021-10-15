from django.shortcuts import render
from django.http import HttpResponse
from forms.models import User

def index(request):
    my_dict = {'insert_me': 'Hello!'}
    return render(request, 'forms/index.html', context=my_dict)

def users(request):
    user_list = User.objects.all()
    my_dict = {'users':user_list}
    return render(request,'forms/forms.html',context=my_dict)