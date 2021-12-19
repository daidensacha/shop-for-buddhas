from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from testimonials.models import Testimonial
# from .forms import ContactForm
# Create your views here.


def index(request):
    """ A view to return the index page """

    testimonials = Testimonial.objects.filter(approved=True)
    context = {
        'testimonials': testimonials,
        'stars': [1, 2, 3, 4, 5],
    }
    return render(request, 'home/index.html', context)


def contact(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')

    # email configurations
    # title = subject
    # body = ("Here is subject {} and comments {}".format(subject,comments))
    # send_mail(title,body,"noreply@gmail.com", [email,"daidensacha@gmail.com"])

    subject = subject
    content = render_to_string('confirmation_emails/contact_email.html', {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'subject': subject,
        'message': message
        })
    email = EmailMessage(subject, content, to=[
                         'daiden@gmail.com', email])
    email.send()

    testimonials = Testimonial.objects.filter(approved=True)
    context = {
        'testimonials': testimonials,
        'stars': [1, 2, 3, 4, 5],
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'subject': subject,
        'message': message,
    }
    return render(request, 'home/index.html', context)


# def ContactFormView(FormView):
#     form = contactForm()

#     context = {
#         "form": ContactForm,
#         }
#     return render(request, "home/index.html", context)