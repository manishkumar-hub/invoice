from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True, required=False)

    class Meta:
        model = Invoice
        fields = '__all__'

    def create(self, validated_data):
        details_data = validated_data.pop('details', [])
        invoice = Invoice.objects.create(**validated_data)
        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)
        return invoice

    def update(self, instance, validated_data):
        details_data = validated_data.pop('details', [])
        details = instance.details.all()
        details = list(details)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.save()

        for detail_data in details_data:
            detail = details.pop(0)
            detail.description = detail_data.get('description', detail.description)
            detail.quantity = detail_data.get('quantity', detail.quantity)
            detail.unit_price = detail_data.get('unit_price', detail.unit_price)
            detail.price = detail_data.get('price', detail.price)
            detail.save()

        return instance
