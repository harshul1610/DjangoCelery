from django.shortcuts import render, HttpResponse
from .tasks import add

# Create your views here.
def addx(request):
	out = add.delay(9000,10000)
	return HttpResponse(out.get())