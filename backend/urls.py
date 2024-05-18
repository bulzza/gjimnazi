from django.urls import path
from . import views
from .views import *

app_name = "backend"

urlpatterns = [
    path("" , views.dashboard, name="dashboard"),
    path("hero/", views.HeroClass.hero , name="hero"),
    path("hero/editHero/<int:pk>", views.HeroClass.editHero, name="editHero"),
    path("hero/addHero/", views.HeroClass.addHero, name="addHero"),
    path('hero/deleteHero/<int:pk>', views.HeroClass.deleteHero, name='deleteHero'),
    path("cta/", views.CtaClass.cta, name="cta"),
    path("cta/editCta/<int:pk>", views.CtaClass.editCta, name="editCta"),
    path("cta/addCta/", views.CtaClass.addCta, name="addCta"),
    path('cta/deleteCta/<int:pk>', views.CtaClass.deleteCta, name='deleteCta'),
    path("aboutus/", views.AboutusClass.aboutus, name="aboutus"),
    path("aboutus/editAboutus/<int:pk>", views.AboutusClass.editAboutus, name="editAboutus"),
    path("aboutus/addAboutus/", views.AboutusClass.addAboutus, name="addAboutus"),
    path('aboutus/deleteAboutus/<int:pk>', views.AboutusClass.deleteAboutus, name='deleteAboutus'),
    path("faq/", views.FaqClass.faq, name="Faq"),
    path("faq/editFaq/<int:pk>", views.FaqClass.editFaq, name="editFaq"),
    path("faq/addFaq/", views.FaqClass.addFaq, name="addFaq"),
    path('faq/deleteFaq/<int:pk>', views.FaqClass.deleteFaq, name='deleteFaq'),
    path("gallery/", views.GalleryClass.gallery, name="gallery"),
    path("gallery/editGallery/<int:pk>", views.GalleryClass.editGallery, name="editGallery"),
    path("gallery/addGallery/", views.GalleryClass.addGallery, name="addGallery"),
    path('gallery/deleteGallery/<int:pk>', views.GalleryClass.deleteGallery, name='deleteGallery'),
    path("users/",views.users, name="users" ),
    path("logout/", views.user_logout, name="logout"),
]