from django.shortcuts import render
from .forms import payForm, TIPForm, InvoiceForm
from .models import payTrio
from hashlib import md5

# Create your views here.
shop_id = 306717
secret = '26sgK9rgTqiIaeTmMy2ww5vXKS261shKV'

def  template(request):
	if request.method == 'POST':
		form  = payForm(request.POST)
		if form.is_valid():
			currency = form.cleaned_data['currency']
			amount = form.cleaned_data['amount']
			description = form.cleaned_data['description']
			print(currency)
			if int(currency) == 978: # EUR' invoice
				payway = 'payeer_eur'
				sign = save_sign(str(amount), str(currency), str(payway), str(shop_id), secret)
				invoice = payTrio(amount = amount, currency = currency, description = description, sign = sign, payway = payway)
				invoice.save()
				qs = payTrio.objects.get(shop_invoice_id=invoice.shop_invoice_id)
				context = {
					'amount': int(qs.amount),
					'currency': int(qs.currency),
					'payway': qs.payway,
					'shop_invoice_id': int(qs.shop_invoice_id),
					'shop_id': int(qs.shop_id),
					'sign': qs.sign
				}
				return render(request, 'index.html', {'context': context,
													'checkPoint': '1'})
			else: # 840 'USD'
				payway = 'payeer_usd'
				sign = save_sign(str(amount), str(currency), str(payway), str(shop_id), secret)
				invoice = payTrio(amount = amount, currency = currency, description = description, sign = sign, payway = payway)
				invoice.save()
				qs = payTrio.objects.get(shop_invoice_id=invoice.shop_invoice_id)
				form = TIPForm(instance=qs)
				return render(request, 'index.html', {'form': form,
													'checkPoint': '1'})
		else:
			return render(request, 'index.html', {'error': 'Not Valid'})
	form  = payForm()
	return render(request, 'index.html', {'form': form})


def save_sign(amount, currency, payway, shop_id, secret):
	unic = (amount+':'+currency+':'+payway+':'+shop_id+secret).encode('utf-8')
	sign = md5(unic).hexdigest()
	return sign


def status(request):
	return render(request, 'status.html', {'massage': 'Активация прошла успешно.'})

