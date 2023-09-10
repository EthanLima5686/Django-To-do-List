from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request): 
    return render(request, 'todoList/home.html', {});
def test(request):
    return render(request, 'todoList/test.html', {});