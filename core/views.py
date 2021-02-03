from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

# Create your views here.
from django.views.generic import ListView, DetailView

from core.models import Product, Category


class HomeView(ListView):
    def get(self, request):
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')
        # products = Product.get_all_products()
        # print(products)
        # return render(request, 'homepage/index.html', {'products': products})


def store(request):
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    products = None
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()
    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'homepage/index_categories.html', data)


# model = Product
# paginate_by = 10
# template_name = "homepage/index.html"


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
