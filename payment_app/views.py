from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import *


class ProductListView(ListView):
    model = Product
    template_name = "payment_app/product_list.html"
    context_object_name = 'product_list'


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    template_name = "payment_app/product_create.html"
    success_url = reverse_lazy("home")


class ProductDetailView(DetailView):
    model = Product
    template_name = "payment_app/product_detail.html"
    pk_url_kwarg = 'id'


class OrderHistoryListView(ListView):
    model = OrderDetail
    template_name = "payment_app/order_history.html"
