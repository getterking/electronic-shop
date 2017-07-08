from django import forms
from .models import Shop, Goods, ShoppingCartItem, Remittance, RemittanceItem

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('name', 'address', 'introduction')

class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('goods_type', 'name', 'price', 'introduction')

class ShoppingCartItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingCartItem
        fields = ('number', )

class RemittanceForm(forms.ModelForm):
    class Meta:
        model = Remittance
        fields = ('address', 'phone', 'message')

