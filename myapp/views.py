from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def service(request):
    return  render(request, 'myapp/service.html')