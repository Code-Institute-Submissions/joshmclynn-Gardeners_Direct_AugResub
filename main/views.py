from django.shortcuts import render, redirect
from .forms import newsletter_form
import sweetify


def index(request):

    form = newsletter_form(request.POST or None)

    context = {
        'form': form
    }
    return render(request, 'home/index.html', context)


def email_add(request):

    if request.method == 'POST':
        form = newsletter_form(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, title='Your Email has been added to the mailing list')
            return redirect('/')
        else:
            sweetify.error(request, title='Cannot add this email to the mailing list(Duplicate)!')
            return redirect('/')
    