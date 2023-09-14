from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NQmeFAbibSpA1zv6nc5kEg1QrrBkds1AsEj3a2W3ihLXmvyGdd74CdQpn1svYdRaWHY2vegntEVIRjdaRrQulkf001rC0ZTUP',
        'client_secret': 'test',
    }

    return render(request, template, context)