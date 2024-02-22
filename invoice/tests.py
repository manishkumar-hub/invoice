from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {'date': '2024-02-22', 'customer_name': 'Test Customer'}
        self.invoice = Invoice.objects.create(**self.invoice_data)
        self.invoice_detail_data = {'invoice': self.invoice.id, 'description': 'Test Description', 'quantity': 2, 'unit_price': 10.0, 'price': 20.0}
        self.invoice_detail = InvoiceDetail.objects.create(**self.invoice_detail_data)

    def test_create_invoice(self):
        url = reverse('invoice-list-create')
        response = self.client.post(url, self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_invoice(self):
        url = reverse('invoice-detail', kwargs={'pk': self.invoice.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invoice_detail(self):
        url = reverse('invoice-detail-list-create')
        response = self.client.post(url, self.invoice_detail_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_invoice_detail(self):
        url = reverse('invoice-detail-detail', kwargs={'pk': self.invoice_detail.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
