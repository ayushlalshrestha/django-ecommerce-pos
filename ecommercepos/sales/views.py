from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ProductSerializer, CustomerSerializer
from .models import Sale, Product, Customer


# Create your views here.


def index(request):
    context = {
        "name": "Ayush Lal Shrestha",
    }
    return render(request, "sales/sale-home.html", context)


class productlistapi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class customerlistapi(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
       pass     
