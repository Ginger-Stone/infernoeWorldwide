from django.shortcuts import render
from django.conf import settings
from django.http import HttpRequest
from django.http import HttpResponseRedirect

from .models import Portfolio, Service, Service2, Service3, Event, InfernoeTeam
from django.views import View
from django.views.generic import ListView, DetailView
from .forms import ContactForm

def index(request):
    latest_service_list = Service.objects.order_by('-id')[:1]
    latest_service2_list = Service2.objects.order_by('-id')[:1]
    latest_service3_list = Service3.objects.order_by('-id')[:1]
    ##latest_portfolio_list = Portfolio.objects.order_by('-id')[:6]
    last = Portfolio.objects.latest()
    latest_id = last.id
    latest_portfolio_list = Portfolio.objects.filter(pk=latest_id)
    latest1_portfolio_list = Portfolio.objects.filter(pk=latest_id-1)
    latest2_portfolio_list = Portfolio.objects.filter(pk=latest_id-2)
    latest3_portfolio_list = Portfolio.objects.filter(pk=latest_id-3)
    latest4_portfolio_list = Portfolio.objects.filter(pk=latest_id-4)
    latest5_portfolio_list = Portfolio.objects.filter(pk=latest_id-5)
    last_event = Event.objects.latest()
    latest_event = last_event.id
    latest_event_list = Event.objects.filter(pk=latest_event)
    latest1_event_list = Event.objects.filter(pk=latest_event-1)
    latest2_event_list = Event.objects.filter(pk=latest_event-2)
    latest3_event_list = Event.objects.filter(pk=latest_event-3)
    last_member = InfernoeTeam.objects.latest()
    latest_member = last_member.id
    latest_member_list = InfernoeTeam.objects.filter(pk=latest_member)
    latest1_member_list = InfernoeTeam.objects.filter(pk=latest_member-1)
    latest2_member_list = InfernoeTeam.objects.filter(pk=latest_member-2)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            your_email = form.cleaned_data['your_email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']

            recipients = ['doreenjeptoo@gmail.com']
            if cc_myself:
                recipients.append(sender)
            send_mail(subject,message, sender, recipients)
            return HttpResponseRedirevt('/thanks/')
    else:
        form = ContactForm()

    context = {'latest_service_list': latest_service_list, 'latest_service2_list': latest_service2_list, 'latest_service3_list': latest_service3_list, 'latest_portfolio_list': latest_portfolio_list, 'latest1_portfolio_list': latest1_portfolio_list, 'latest2_portfolio_list': latest2_portfolio_list, 'latest3_portfolio_list': latest3_portfolio_list, 'latest4_portfolio_list': latest4_portfolio_list, 'latest5_portfolio_list': latest5_portfolio_list,
            'latest_event_list': latest_event_list, 'latest1_event_list': latest1_event_list, 'latest2_event_list': latest2_event_list, 'latest3_event_list': latest3_event_list, 'latest_member_list': latest_member_list, 'latest1_member_list': latest1_member_list, 'latest2_member_list': latest2_member_list, 'form':form}

   
    ##last = Portfolio.objects.latest()
    ##latest_id = last.id
    ##portfolio = Portfolio.objects.get(pk=latest_id)
    return render(request, 'infernoeWorldwide/index.html', context)
