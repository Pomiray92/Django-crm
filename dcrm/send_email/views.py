from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import NotificationForm
from django.conf import settings


# Create your views here.
def send(request):
    
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data['recipient']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(
                subject=subject,
                message=message.title(),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[recipient],
                )
            form.save()
            # messages.success(request, "You are logged in")
            return render(request, 'send_app/success.html')
    else:
        form = NotificationForm()
    return render(request, 'send_app/create_notification.html', {'form': form})