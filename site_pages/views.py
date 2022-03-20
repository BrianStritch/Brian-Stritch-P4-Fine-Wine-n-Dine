from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserChangeForm
from .forms import UserAccountDetailsForm, EditProfileForm



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


class Profile(TemplateView):
    template_name = 'nannys_alternative/profile.html'


"""
SIgn Up template with form which allows users to input a username, first name, last name
email address and a password with a password verifcation check.
"""

class Sign_up(TemplateView):
    template_name = 'nannys_alternative/edit_profile.html'

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


"""
Edit profile template with form which allows users to Edit their username, first name, last name
email address and a password with a password verifcation check.
"""

class Edit_profile(TemplateView):
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

"""

"""
 