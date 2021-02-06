from django.urls import path, include
from core.views import HomeView, LoginView, RegisterView, CartView, CheckoutView, ItemDetailView, store, logout
from .middlewares.auth import auth_middleware

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('cart', auth_middleware(CartView.as_view()), name='cart'),
    path('checkout', auth_middleware(CheckoutView.as_view()), name='checkout'),
    path('product/<slug>', ItemDetailView.as_view(), name='product'),
    path('store', store, name='store'),
    path('logout', logout, name='logout'),
]
