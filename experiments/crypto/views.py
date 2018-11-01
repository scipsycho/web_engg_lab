from django.shortcuts import render
from django.http import HttpResponse

from .forms import *
import subprocess

# Create your views here.
#Default view for the homepage
def index(request):
    return render(request,'crypto/index.html')

def rsa(request):
    
    if request.method == 'POST':

        form = rsaInput(request.POST)

        if form.is_valid():
            return render(request, 'crypto/output.html',{ 'output': 'I am here', 'algo':'rsa'})



    else:
        form = rsaInput()


    return render(request, 'crypto/enc.html', {'form': form , 'heading':'rsa'})


def des(request):

    if request.method == 'POST':

        form = desInput(request.POST)

        if 'encrypt' in request.POST:
            encrypt = True
        else:
            encrypt = False
        if form.is_valid():
           
            if encrypt:
                output = subprocess.check_output(['./crypto/enc_command_line',form.cleaned_data.get('message'),form.cleaned_data.get('key')])
                output = str(output)[2:-1]
            else:
                output = subprocess.check_output(['./crypto/dec_command_line',form.cleaned_data.get('message'),form.cleaned_data.get('key')])
                output = str(output)[2:-1]
                for i in range(len(output)):
                    if output[i] == '\\' :
                        output = output[:i]
                        break
            return render(request, 'crypto/output.html', {'output': str(output), 'algo': 'des'})


    else:
        form = desInput()


    return render(request, 'crypto/enc.html', {'form':form, 'heading':'des'})

