import json

from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View

from hbs.settings import DEFAULT_FROM_EMAIL
from .forms import ContactForm


class SystemView(View):
    def get(self, request):
        return render(request, 'sites/O-systemie.html')

class HBSView(View):
    def get(self, request):
        context = {
            'kontakt': ContactForm(),
        }
        return render(request, 'sites/index.html', context)

    def post(self, request):
        contact_form = ContactForm(request.POST)

        context = {
            'kontakt': contact_form
        }

        if contact_form.is_valid():
            form = contact_form.save(commit=False)
            mail_content = {
                'imie': form.imie,
                'email': form.email,
                'tresc': form.tresc,
            }

            form.save()

            message = render_to_string('sites/mail/mail.html', mail_content)

            send_mail(
                subject='Wiadomość z formularza kontaktowego HBS.',
                message='',
                from_email=DEFAULT_FROM_EMAIL,
                recipient_list=['info@hbspolska.org.pl'],
                fail_silently=False,
                html_message=message
            )

            return HttpResponseRedirect(reverse_lazy("hbs"))

