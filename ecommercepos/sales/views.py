from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic.detail import DetailView
from.forms import ProductForm, MyRegistrationForm
from .models import Sale, Product, Customer
from .serializer import ProductSerializer, CustomerSerializer, SaleSerializer


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        if self.request.user.is_authenticated():
            login_status = self.request.user.first_name + " " + self.request.user.last_name
        elif not self.request.user.is_authenticated():
            login_status = "Guest User"   
        else:
            pass
        context["login_status"] = login_status         
        return context


# New User Creation
def new_user_creation(request):
    if request.method == "POST":
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/admin/")
        else:
            raise forms.ValidationError("Some Error during Data Entry !!")    
    else:
        form = MyRegistrationForm()
        context = {
            "form" : form,
        }
        return render(request, "sales/newregister.html", context)


@login_required
def safearea(request):
    print(request.user.first_name + " - - - - - - - - - -  - - - - - - - - - -  - - - - - ")
    return HttpResponseRedirect('/sales/')


# ------------------------ Sending and Email Test------------------------------------------ 
def sendemail(request):
    send_mail(
    'Sending email via. django',
    'Automation test 001 - Hello Manaish - <h1>Ayush Lal Shrestha</h1>',
    'artifice.tundra@gmail.com',
    ['manish.shakya534@gmail.com', ],
    fail_silently = False,
    )    
    return HttpResponse("<h1>Automated Email Success !!</h1>")

def index(request):
    print(request.COOKIES)
    print( " ---------------------------------------------- This is COOKIES")
    if(request.session is not None):
        print("Some Session is defo there !!")
    if request.user.is_authenticated:
        name = request.user.first_name
    else:
        name = "you are not logged-in !!"     
    context = {
        "name": name,
    }
    return render(request, "sales/sale-home.html", context)

# ------------------------ Adding new Product via. a Form ---------------------------------------------- 
def newproduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit = False) # So that changes can be made before saving
            instance.save()
    else:
        form = ProductForm()
        context = {
        "form" : form,
    }
        response = render(request, "sales/new-product.html", context)
        request.session["seesiones_id"] = "Ayush Session SHR"
        response.set_cookie("superduperusername", "Ayush SHR")

    return response

# ------------------------ Sessions and Cookies Test ---------------------------------------------- 
def cookiesandsessions(request):
    response =  HttpResponse("Cookies and Sessions Test")
    response.set_cookie("name", "Ayush Lal Shrestha")
    return response


# ------------------------ REST Services ---------------------------------------------- 
class productlistapi(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class customerlistapi(APIView):
    def get(self, request):
        #print(request.COOKIES)
        customers = Customer.objects.all()
        serialized = CustomerSerializer(customers, many=True)
        return Response(serialized.data)

    def post(self, request):
        pass

class salelistapi(ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer