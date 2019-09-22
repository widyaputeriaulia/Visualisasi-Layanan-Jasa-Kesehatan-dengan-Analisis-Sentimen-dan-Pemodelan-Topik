from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from . import read

def index(request):
	return render(request,'dashboard.html')
	
def index01(request):
	return render(request,'bethesda.html')

def index02(request):
	return render(request,'jih.html')

def index03(request):
	return render(request,'kota.html')

def index04(request):
	return render(request,'panembahan.html')

def index05(request):
	return render(request,'panti_rapih.html')

def index06(request):
	return render(request,'pau_hardjolukito.html')

def index07(request):
	return render(request,'pku_muhammadiyah.html')

def index08(request):
	return render(request,'sardjito.html')

def index09(request):
	return render(request,'sleman.html')

def index010(request):
	return render(request,'ugm.html')

def index011(request):
	return render(request, 'wates.html')

def coba(request):
	return render(request, 'coba.html')



