from django.shortcuts import render, get_object_or_404, reverse
from django.template.defaultfilters import slugify
from django.views import generic, View
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

# Create your views here.

class Home(TemplateView):
    template_name = 'index.html'
   
class Menu(TemplateView):
    template_name = 'nannys_alternative/menu.html'


class OpeningHours(TemplateView):
    template_name = 'nannys_alternative/opening-times.html'

   
class ProductsPage(TemplateView):
    template_name = 'about.html'


class Contact(TemplateView):
    template_name = 'user_account_details.html'


class User_account_details(TemplateView):
    template_name = 'user_account_details.html'
