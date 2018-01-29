from django.shortcuts import render
from .forms import ContactForm

def index(request):
    form = ContactForm()
    return render(request, 'index.html', {'form': form})