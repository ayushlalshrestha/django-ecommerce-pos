from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
	context = {
		"name": "Ayush Lal Shrestha",
	}
	return render(request, "sales/sale-home.html", context)
