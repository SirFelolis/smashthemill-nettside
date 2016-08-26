from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<b>Rango</b> says hey there world! <br> <a href='/testapp/about'>About!</a>")
	
def about(request):
	return HttpResponse("Rango says that this is the about page! <br> <a href='/testapp'>Return!</a>")