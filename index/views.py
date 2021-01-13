from django.shortcuts import render
from . forms import ContactForm
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse

# Create your views here.


def home_view(request):
    # If user has filled the email form and wants to post it
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

# Process Email send
            try:
                send_mail(subject, message, email, ['tlotlegomgp@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'index/email_sent.html')

    # Else Present empty form to user
    else:
        form = ContactForm()

    return render(request, 'index/index.html', {'form': form})
