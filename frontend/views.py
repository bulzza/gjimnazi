from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from .models import *  # Import your model
from backend.models import *
from django.contrib.auth.decorators import login_required

from .models import ContactMessage
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

# Index/  main page
def index(request):

    querysetHero = Hero.objects.all()
    querysetCta = Cta.objects.all()
    querysetAboutus = Aboutus.objects.all() 
    querysetFaq = Faq.objects.all()


    context = {
        'heroes': querysetHero,
        'ctas': querysetCta,
        'aboutuss': querysetAboutus,
        'faqs': querysetFaq,
        'page_name': 'Gjimnazi',
    }

    
    return render(request, 'index.html', context)

def news(request):
     
    context = {
        'page_name': 'News and Updates'
    }

    return render(request, 'news.html', context)

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save the contact information to the database
        contact_message = ContactMessage(name=name, email=email, message=message)
        contact_message.save()
        
        # Send email
        subject = 'Gjimnazi Contact Notification'
        body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        from_email = 'bulzaabdilii@gmail.com'  # Update with your email
        to_email = ['agoonn98@gmail.com']  # Update with recipient email(s)
        
        send_mail(subject, body, from_email, to_email, fail_silently=False)
        
        return HttpResponse('Thank you for your message! We will get back to you soon.')
    
    context = {
        'contact': 'Contact Us'
    }
    
    return render(request, 'contact.html', context)

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = user.username  # Store username in session
                return redirect('/cms/')  # Redirect to desired URL after login
           
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
