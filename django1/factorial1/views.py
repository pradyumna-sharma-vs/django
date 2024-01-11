from django.shortcuts import render
def home(request):
    return render(request,'factorial1/index.html',{'param1':"hello world"})
# Create your views here.
