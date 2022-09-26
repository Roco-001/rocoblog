from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from .models import Contact
from .forms import ContactForm
# Create your views here.


def contact(request):
    contact_form = ContactForm
    if request.method == "POST":
        contact_form = contact_form(data=request.POST)

        # Validamos el formulario
        if contact_form.is_valid():
            cd = contact_form.cleaned_data

            subject = f"DESDE EL BLOG ZENBLOG:{cd['subject']}"

            message = f"EL Sr(a) {cd['name']}\U00002757\n\n Comento lo siguiente:\n\n{cd['content']}"
            # Lo enviamos y redireccionamos
            try:
                send_mail(subject, message, 'rocoweb@outlook.com',
                          ['rocoweb@outlook.com','rodrigojrodriguezm@gmail.com'])
                Contact.objects.create(
                                        name=cd['name'],
                                        email=cd['email'],
                                        subject=cd['subject'],
                                        content=cd['content']
                                    )
                return redirect(reverse('contact:contact') + "?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact:contact') + "?fail")
    context = {
        'form': contact_form,
    }
    return render(request, "contact/contact.html", context)