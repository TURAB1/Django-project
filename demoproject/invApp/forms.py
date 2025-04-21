from django import forms
from api.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =['id', 'name', 'description', 'price', 'stock']
        labels = {
            'id': 'Product ID',
            'name': 'Name',
            'description': 'Description',
            'price': 'Price',
            'stock': 'Stock',
        }
        widgets = {
            'id': forms.NumberInput(
                attrs={'placeholder': 'e.g. 1', 'class': 'form-control'}),
            'name': forms.TextInput(
                attrs={'placeholder': 'e.g. shirt', 'class': 'form-control'}),
            'description': forms.TextInput(
                attrs={'placeholder': 'e.g. Facere recusandae', 'class': 'form-control'}),
            'price': forms.NumberInput(
                attrs={'placeholder': 'e.g. 19.99', 'class': 'form-control'}),
            'stock': forms.NumberInput(
                attrs={'placeholder': 'e.g. 10','class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if isinstance(self.instance, Product):  # Ensure it's an instance of Product
           #self.fields['id'].widget.attrs['value'] = self.instance.id
            self.fields['name'].widget.attrs['value'] = self.instance.name
            self.fields['description'].widget.attrs['value'] = self.instance.description
            self.fields['price'].widget.attrs['value'] = self.instance.price
            self.fields['stock'].widget.attrs['value'] = self.instance.stock
            print(f"name: {self.instance.name}")