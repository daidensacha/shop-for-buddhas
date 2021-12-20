from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from testimonials.models import Testimonial
from profiles.models import Contact
from profiles.forms import ContactForm


def index(request):
    """ A view to return the index page """

    testimonials = Testimonial.objects.filter(approved=True)
    context = {
        'testimonials': testimonials,
        'stars': [1, 2, 3, 4, 5],
    }
    return render(request, 'home/index.html', context)


def contact(request):
    """ Create the contact form view on homepage """
    form = ContactForm()
    """ Process the posted form data """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            subject = request.POST['subject']
            content = render_to_string(
                'confirmation_emails/contact_email.html', {
                    'first_name': request.POST['first_name'],
                    'last_name': request.POST['last_name'],
                    'sender': request.POST['sender'],
                    'subject': request.POST['subject'],
                    'message': request.POST['message']
                })
            email = EmailMessage(subject, content, to=[
                                'daiden@gmail.com', request.POST['sender']])
            messages.success(request, f'Thanks {request.POST["first_name"]}, \
                                       your message has been posted.')
            email.send()

            form.save()

    testimonials = Testimonial.objects.filter(approved=True)
    context = {
        'testimonials': testimonials,
        'stars': [1, 2, 3, 4, 5],
        'form': form,
    }
    return render(request, 'home/index.html', context)
