from django.shortcuts import render

from .forms import SubscriptionForm


def subscribe(request):
    template_name = 'subscriptions/subscription_form.html'
    context = {'form': SubscriptionForm()}
    return render(request, template_name, context=context)
