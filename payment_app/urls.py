from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('detail/<id>/', ProductDetailView.as_view(), name='detail'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('history/', OrderHistoryListView.as_view(), name='history'),
]