from django.shortcuts import render
from .models import Starters, Breakfast, Lunch, \
    Dinner, Testimonials, Events, Chefs, Gallery
from .forms import Book_A_TableForm, ContactForm


# Create your views here.
def IndexView(request):
    starters = Starters.objects.all()
    breakfast = Breakfast.objects.all()
    lunch = Lunch.objects.all()
    dinner = Dinner.objects.all()
    testimonials = Testimonials.objects.all()
    events = Events.objects.all()
    chefs = Chefs.objects.all()
    gallery = Gallery.objects.all()

    book_a_tableform = Book_A_TableForm()
    contacts = ContactForm()

    context = {
        # Models
        'starters': starters,
        'breakfasts': breakfast,
        'lunchts': lunch,
        'dinners': dinner,
        'testimonials': testimonials,
        'events': events,
        'chefs': chefs,
        'galleryes': gallery,

        # Forms
        'book_a_tableform': book_a_tableform,
        'contacts': contacts,
    }
    return render(request, 'index.html', context=context)