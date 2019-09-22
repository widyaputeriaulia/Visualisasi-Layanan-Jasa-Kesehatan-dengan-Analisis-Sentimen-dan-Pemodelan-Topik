from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

def index(request):
	context = {

	}
	return render(request,'dashboard.html',context)