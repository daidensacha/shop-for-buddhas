from django.shortcuts import render, redirect
from .forms import TestimonialForm
from .models import Testimonial
# Model Testimonial imported but unused?


def testimonial_view(request):
    """Create form view, and post data"""
    form = TestimonialForm()
    if request.method == "POST":
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form_1 = form.save(commit=False)
            form_1.user = request.user
            form_1.save()
            return redirect("home")

    context = {
        "form": TestimonialForm,
    }
    return render(request, "testimonial.html", context)
