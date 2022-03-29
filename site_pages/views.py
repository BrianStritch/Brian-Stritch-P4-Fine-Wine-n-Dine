from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import UserCreationForm, UserAccountDetailsForm, EditProfileForm


class Home(TemplateView):
    template_name = 'index.html'
        
    


class Menu(TemplateView):
    template_name = 'nannys_alternative/menu.html'


class OpeningHours(TemplateView):
    template_name = 'nannys_alternative/opening-times.html'


class ProductsPage(TemplateView):
    template_name = 'nannys_alternative/about.html'


class About(TemplateView):
    template_name = 'nannys_alternative/about.html'





class Sign_up(TemplateView):
    """
    SIgn Up template with form which allows users to input a username,
    first name, last name, email address and a password with a password
    verifcation check.
    """    
    template_name = 'nannys_alternative/sign_up.html'

    def get(self, request):
        form = UserAccountDetailsForm()
        return render(
            request,
            self.template_name,
            {
                'form': form,
            })

    def post(self, request):
        if request.method == 'POST':
            form = UserAccountDetailsForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('home'))

        else:
            form = UserAccountDetailsForm()
            details = {
                'form': form,
            }
            return render(request, self.template_name, details)


class Profile(TemplateView):
    """
    class to return a rendered tempate view of the Index or 'home' page
    """
    template_name = 'nannys_alternative/profile.html'


class Edit_profile(TemplateView):
    """
    Edit profile template with form which allows users to Edit their username,
    first name, last name, email address and a password with a password
    verifcation check.
    """
    template_name = 'nannys_alternative/edit_profile.html'

    def get(self, request):
        form = EditProfileForm()
        return render(
            request,
            self.template_name,
            {
                'form': form,
            })

    def post(self, request):
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('profile'))

        else:
            form = EditProfileForm(instance=request.user)
            details = {
                'form': form,
            }
            return render(request, self.template_name, details)

class DeleteProfile(DeleteView):
    model = User
    template_name = 'nannys_alternative/delete_profile.html'
    success_url = reverse_lazy('home')


