# -*- coding: utf-8 -*-
from django.db import models
from hashlib import md5
from decimal import Decimal

# Create your models here.

class payTrioManager(models.Model):
	@classmethod
	def save_sign(self, amount, currency, payway, shop_id):
		self.sign = md5.hexdigest(amount+':'+currency+':'+payway+':'+shop_id)
		save = self.save()
		return save


choices = (
    (840, ("USD")),
    (978, ("EUR"))
)


class payTrio(models.Model):
	amount = models.DecimalField(max_digits = 1000000, decimal_places = 2) # сумма 
	payway = models.CharField(max_length = 100, default = 'Card') # способ оплаты
	description = models.TextField(max_length = 5000, default = '')	# описаниеdf
	currency = models.CharField(max_length = 3, default = 'USD') # валюта
	shop_id = models.IntegerField(default = 306717) # индинтификация магазина
	shop_invoice_id = models.AutoField(primary_key=True)
	sign = models.CharField(max_length = 10000) # hex
	date = models.DateTimeField(auto_now = True)
	objects = payTrioManager()


	class Meta:
		verbose_name = 'Payment'

	def __str__(self):
		return self.shop_invoice_id	

