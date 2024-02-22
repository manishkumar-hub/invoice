from django.urls import path
from .views import (
    InvoiceListCreateAPIView,
    InvoiceDetailAPIView,
    InvoiceDetailListCreateAPIView,
    InvoiceDetailDetailAPIView
)

urlpatterns = [
    path('invoices/', InvoiceListCreateAPIView.as_view(), name='invoice-list-create'),
    path('invoices/<int:pk>/', InvoiceDetailAPIView.as_view(), name='invoice-detail'),
    path('invoice-details/', InvoiceDetailListCreateAPIView.as_view(), name='invoice-detail-list-create'),
    path('invoice-details/<int:pk>/', InvoiceDetailDetailAPIView.as_view(), name='invoice-detail-detail'),
]
