# coding: utf-8
from django.forms import ModelForm
from django import forms
from .models import payTrio

choices = (
    (840, ("USD")),
    (978, ("EUR"))
)


class payForm(ModelForm):
	currency = forms.ChoiceField(choices =choices)

	class Meta:
		model = payTrio
		fields = ['amount','description','currency']


class TIPForm(ModelForm):
    shop_invoice_id = forms.IntegerField()
    class Meta:
        model = payTrio
        fields =  ['amount','currency','shop_id', 'shop_invoice_id', 'sign']


class InvoiceForm(ModelForm):
    shop_invoice_id = forms.IntegerField()
    class Meta:
        model = payTrio
        fields =  ['amount', 'currency', 'payway', 'shop_id', 'shop_invoice_id', 'sign']

