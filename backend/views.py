from django.shortcuts import render, redirect,get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
# from .froms import *
from django.views.decorators.csrf import csrf_exempt
from .models import *  # Import your model
from .forms import *
from django.contrib.auth.decorators import login_required



@login_required(login_url = '/login/')
# Index/  main page
def dashboard(request):
    return render(request, 'base.html')


class HeroClass:
    
    @login_required(login_url='/login/')
    def hero(request):
        querysetHero = Hero.objects.all()
        context = {
            'heroes': querysetHero,
            'page_name': "Hero"
        }
        return render(request, 'hero/hero.html', context)

    @login_required(login_url='/login/')
    def editHero(request, pk):
        context = {
            'page_name': "Edit Hero"
        }

        instance = get_object_or_404(Hero, pk=pk)
        if request.method == 'POST':
            form = HeroForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('/cms/hero/')  # Redirect to a success URL
        else:
            form = HeroForm(instance=instance)
        return render(request, 'hero/editHero.html', {'form': form})

    @login_required(login_url='/login/')
    def addHero(request):
        if request.method == 'POST':
            form = HeroForm(request.POST, request.FILES)
            if form.is_valid():
                hero = form.save(commit=False)
                hero.created_by = request.user
                hero.save()
                return redirect('/cms/hero/')
        else:
            form = HeroForm()
        return render(request, 'hero/addHero.html', {'form': form})

    @login_required(login_url='/login/')
    def deleteHero(request, pk):
        hero = get_object_or_404(Hero, pk=pk)
        hero.delete()
        return redirect('/cms/hero/')

class CtaClass: 

    @login_required(login_url = '/login/')
    def cta(request):
        querySetCta = Cta.objects.all()

        context = {
            'ctas': querySetCta,  # Rename queryset to heroes for clarity
            'page_name': "Call to Action"
        }

        return render(request, "cta/cta.html", context)
    
    @login_required(login_url='/login/')
    def editCta(request, pk):
        instance = get_object_or_404(Cta, pk=pk)
        if request.method == 'POST':
            form = CtaForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('/cms/cta/')  # Redirect to a success URL
        else:
            form = CtaForm(instance=instance)
        return render(request, 'cta/editCta.html', {'form': form})
   
    @login_required(login_url='/login/')
    def addCta(request):
        if request.method == 'POST':
            form = CtaForm(request.POST, request.FILES)
            if form.is_valid():
                cta = form.save(commit=False)
                cta.created_by = request.user
                cta.save()
                return redirect('/cms/cta/')
        else:
            form = CtaForm()

        return render(request, 'cta/addCta.html', {'form': form})
 
    @login_required(login_url='/login/')
    def deleteCta(request, pk):
        cta = get_object_or_404(Cta, pk=pk)
        cta.delete()
        return redirect('/cms/cta/')

class AboutusClass: 

    @login_required(login_url = '/login/')
    def aboutus(request):
        querySetAboutus = Aboutus.objects.all()

        context = {
            'aboutuss': querySetAboutus,  # Rename queryset to heroes for clarity
            'page_name': "About Us"
        }

        return render(request, "aboutus/aboutus.html", context)
    
    @login_required(login_url='/login/')
    def editAboutus(request, pk):
        instance = get_object_or_404(Aboutus, pk=pk)
        if request.method == 'POST':
            form = AboutusForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('/cms/aboutus/')  # Redirect to a success URL
        else:
            form = AboutusForm(instance=instance)
        return render(request, 'aboutus/editAboutus.html', {'form': form})
   
    @login_required(login_url='/login/')
    def addAboutus(request):
        if request.method == 'POST':
            form = AboutusForm(request.POST, request.FILES)
            if form.is_valid():
                aboutus = form.save(commit=False)
                aboutus.created_by = request.user
                aboutus.save()
                return redirect('/cms/aboutus/')
        else:
            form = AboutusForm()

        return render(request, 'aboutus/addAboutus.html', {'form': form})
 
    @login_required(login_url='/login/')
    def deleteAboutus(request, pk):
        aboutus = get_object_or_404(Aboutus, pk=pk)
        aboutus.delete()
        return redirect('/cms/aboutus/')

class FaqClass:
    
    @login_required(login_url = '/login/')
    def faq(request):
        querySetFaq = Faq.objects.all()

        context = {
            'faqs': querySetFaq,  # Rename queryset to heroes for clarity
            'page_name': "Frequently Asked Questions"
        }

        return render(request, "faq/faq.html", context)
    
    @login_required(login_url='/login/')
    def editFaq(request, pk):
        instance = get_object_or_404(Faq, pk=pk)
        if request.method == 'POST':
            form = FaqForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('/cms/faq/')  # Redirect to a success URL
        else:
            form = FaqForm(instance=instance)
        return render(request, 'faq/editFaq.html', {'form': form})
   
    @login_required(login_url='/login/')
    def addFaq(request):
        if request.method == 'POST':
            form = FaqForm(request.POST, request.FILES)
            if form.is_valid():
                Faq = form.save(commit=False)
                Faq.created_by = request.user
                Faq.save()
                return redirect('/cms/faq/')
        else:
            form = FaqForm()

        return render(request, 'faq/addFaq.html', {'form': form})
 
    @login_required(login_url='/login/')
    def deleteFaq(request, pk):
        faq = get_object_or_404(Faq, pk=pk)
        faq.delete()
        return redirect('/cms/faq/')



@login_required(login_url = '/login/')
def offers(request):

    context = {
        'page_name': "Offers"
    }
    return render(request, "offers/offers.html", context)

@login_required(login_url = '/login/')
def timeline(request):

    context = {
        'page_name': "Timeline"
    }
    return render(request, "timeline/timeline.html", context)

@login_required(login_url = '/login/')
def directions(request):

    context = {
        'page_name': "Directions"
    }
    return render(request, "directions/directions.html", context)

@login_required(login_url = '/login/')
def team(request):

    context = {
        'page_name': "Team"
    }
    return render(request, "team/team.html", context)

@login_required(login_url = '/login/')
def gallery(request):

    context = {
        'page_name': "Gallery"
    }
    return render(request, "gallery/gallery.html", context)

@login_required(login_url = '/login/')
def news(request):

    context = {
        'page_name': "News and Updates"
    }
    return render(request, "news/news.html", context)

@login_required(login_url = '/login/')
def users(request):

    all_users = User.objects.all()  # This will get all users from the auth system
    
    context = {
        'page_name': "Users",
        'all_users': all_users  # Add the users to the context
    }
    return render(request, "users/users.html", context)

# logout page
def user_logout(request):
    logout(request)
    return redirect('/login/')