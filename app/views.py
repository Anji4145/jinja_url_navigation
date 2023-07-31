from django.shortcuts import render

# Create your views here.
def url_navigation(request):
    return render(request,'url_navigation.html')
def navigation2(request):
    return render(request,'navigation2.html')