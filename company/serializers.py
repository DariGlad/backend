from rest_framework import serializers

from company.models import Products, Company, Contact


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    contacts = ContactsSerializer(required=True)

    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ('id', 'debt', 'create_date')

    def create(self, validated_data):
        contacts = validated_data.pop("contacts")
        contact = Contact.objects.create(**contacts)
        provider = Company.objects.create(contacts=contact, **validated_data)
        return provider


class ProviderUpdateSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    contacts = ContactsSerializer(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ('id', 'debt', 'create_date')
