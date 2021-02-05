from django.urls import path, include
from core.views import HomeView, LoginView, RegisterView, CartView, CheckoutView, ItemDetailView, store, logout

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('store', store, name='store'),
    path('logout', logout, name='logout'),
]
