from django.shortcuts import render
def home(request):
    result=1
    n1=5
    for i in range(1,n1+1,1):
        result=result*i
    return render(request,'html/index.html',{'param1':result,'param2':n1})
        
