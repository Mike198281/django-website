from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail


from . import forms

# Create your views here.
def index(request):
    return render(request,'my_app/index.html')

def services(request):
    return render(request,'my_app/services.html')
    
def about(request):
    return render(request,'my_app/about.html')
    
def contact_us(request):
    form = forms.ContactForm()
    
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            
            full_message = f"""
            Received message below from {name}, {email}
            ________________________


            {message}
            """
            send_mail(
                subject="Received contact form submission",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.NOTIFY_EMAIL],
            )
            return redirect('my_app:success')
        
    return render(request,'my_app/contact_us.html',{'form':form})

def success(request):
    return render(request,'my_app/success.html')

