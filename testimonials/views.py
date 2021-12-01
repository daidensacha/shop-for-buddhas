from django.shortcuts import render, redirect
from .forms import TestimonialForm
from .models import Testimonial
from django.contrib.auth.decorators import login_required
from datetime import datetime
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
            # form_1.created_at = datetime.now
            form_1.save()
            return redirect("home")

    context = {
        "form": TestimonialForm,
    }
    return render(request, "testimonials/testimonial-form.html", context)
