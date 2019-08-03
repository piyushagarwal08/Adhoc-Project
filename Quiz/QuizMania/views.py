from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# Creating first Index page of the website
def index(request):
    return render(request,"QuizMania/index.html")
    #return HttpResponse("Hello")

def test(request):
    return render(request,'QuizMania/Question-page.html')
