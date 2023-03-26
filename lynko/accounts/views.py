from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import SignupForm

import stripe
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CheckoutForm
from djstripe.models import APIKey

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Get form data
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            zipcode = form.cleaned_data['zipcode']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            country = form.cleaned_data['country']
            token = form.cleaned_data['stripeToken']
            product_id = 'prod_1234567890'  # Replace with your product ID
            price_id = 'price_1234567890'  # Replace with your price ID

            try:
                # Create Stripe Customer
                customer = stripe.Customer.create(
                    email=email,
                    name=name,
                    address={
                        'line1': address,
                        'postal_code': zipcode,
                        'city': city,
                        'state': state,
                        'country': country,
                    },
                    source=token
                )

                # Charge Customer
                charge = stripe.Charge.create(
                    amount=1000,  # Replace with your item price in cents
                    currency='usd',
                    customer=customer.id,
                    product=product_id,
                    description='Example Charge'
                )

                # Redirect to Success Page
                messages.success(request, 'Payment Successful.')
                return redirect(reverse('success'))

            except stripe.error.CardError as e:
                # Display error message to user
                messages.error(request, e.error.message)

    else:
        form = CheckoutForm()

    return render(request, 'accounts/checkout.html', {'form': form, 'stripe_public_key': settings.STRIPE_LIVE_SECRET_KEY})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('accounts:login')
    else:
        form = SignupForm()

    
    return render(request, 'accounts/signup.html',{
        'form':form,
    })

