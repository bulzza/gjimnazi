from django.contrib import admin
from .models import *

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'created_by')


@admin.register(Cta)
class CtaAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'created_by')


@admin.register(Aboutus)
class AboutusAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'created_by')


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at', 'created_by')