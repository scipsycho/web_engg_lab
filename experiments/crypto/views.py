from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Default view for the homepage
def index(request):
    return render(request,'crypto/index.html')

def rsa(request):
    return render(request,'crypto/rsa.html')
