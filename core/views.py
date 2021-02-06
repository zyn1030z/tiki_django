from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
from django.views.generic import ListView, DetailView

from core.models import Product, Category, CustomerUser


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
    # print('you are : ', request.session.get('email'))
    username = None

    return render(request, 'homepage/index_categories.html', data)


# model = Product
# paginate_by = 10
# template_name = "homepage/index.html"


class LoginView(View):
    return_url = None

    def get(self, request):
        LoginView.return_url = request.GET.get('return_url')
        categories = Category.get_all_categories()
        data = {}
        data['categories'] = categories

        return render(request, 'homepage/login.html', data)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = CustomerUser.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                if LoginView.return_url:
                    return HttpResponseRedirect(LoginView.return_url)
                else:
                    LoginView.return_url = None
                    return redirect('core:home')
            else:
                error_message = 'Thông tin đăng nhập không đúng!!!'
        else:
            error_message = 'Thông tin đăng nhập không đúng!!!'

        print(email, password)
        return render(request, 'homepage/login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('core:login')


class RegisterView(View):
    def get(self, request):
        RegisterView.return_url = request.GET.get('return_url')
        categories = Category.get_all_categories()
        data = {}
        data['categories'] = categories

        return render(request, 'homepage/register.html', data)

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        address = postData.get('address')

        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
            'address': address
        }
        error_message = None
        customer = CustomerUser(first_name=first_name,
                                last_name=last_name,
                                username=first_name,
                                phone_number=phone,
                                email=email,
                                password=password,
                                address=address)
        error_message = self.validateCustomer(customer)
        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('core:home')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'homepage/register.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif len(customer.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone_number:
            error_message = 'Phone Number required'
        elif len(customer.phone_number) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message


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
