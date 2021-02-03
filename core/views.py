from django.shortcuts import render
from django.views import View

# Create your views here.
from django.views.generic import ListView, DetailView

from core.models import Product


class HomeView(ListView):
    # def get(self, request):
    #     return render(request, 'homepage/index.html')
    model = Product
    paginate_by = 10
    template_name = "homepage/index.html"


class LoginView(View):
    def get(self, request):
        return render(request, 'homepage/login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'homepage/register.html')


# class ProductView(View):
#     def get(self, request):
#         return render(request, 'homepage/product.html')


class CartView(View):
    def get(self, request):
        return render(request, 'homepage/cart.html')


class CheckoutView(View):
    def get(self, request):
        return render(request, 'homepage/checkout.html')


class ItemDetailView(DetailView):
    model = Product
    template_name = "homepage/product.html"
