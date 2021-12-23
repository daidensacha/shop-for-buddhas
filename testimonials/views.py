# from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TestimonialForm
# from .models import Testimonial


# Model Testimonial imported but unused?


@login_required
def testimonial_view(request):
    """Create form view, and post data"""
    form = TestimonialForm()
    if request.method == "POST":
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form_1 = form.save(commit=False)
            form_1.user = request.user
            form_1.save()
            messages.success(request, 'Testimonial submitted successfully.')
            return redirect('home')

    context = {
        'form': TestimonialForm,
    }
    return render(request, 'testimonials/testimonial_form.html', context)
