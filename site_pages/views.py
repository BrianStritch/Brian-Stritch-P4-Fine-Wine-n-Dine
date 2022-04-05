"""
    imports  -------------site_pages views.py----------------------
"""
# third party imports
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.views.generic import TemplateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
# internal imports
from reviews.models import Review
from .forms import UserAccountDetailsForm, EditProfileForm


class Home(TemplateView):
    """
        Class based view to render the home/index page
    """
    template_name = 'index.html'


class Menu(TemplateView):
    """
        Class based view to render the menu page
    """
    template_name = 'nannys_alternative/menu.html'


class OpeningHours(TemplateView):
    """
        Class based view to render the opening hours page
    """
    template_name = 'nannys_alternative/opening-times.html'


class Gallery(generic.ListView):
    """
        Class based view to render the gallery page to display
        a gallery of all images submitted in reviews
    """
    template_name = 'nannys_alternative/gallery.html'
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    paginate_by = 6


class About(TemplateView):
    """
        Class based view to render the about page
    """
    template_name = 'nannys_alternative/about.html'


class SignUp(TemplateView):
    """
    SIgn Up template with form which allows users to input a username,
    first name, last name, email address and a password with a password
    verifcation check.
    """
    template_name = 'nannys_alternative/sign_up.html'

    def get(self, request, *args, **kwargs):
        """
        GET request for rendering the sign up
        page including the User account details form
        """
        form = UserAccountDetailsForm()
        return render(
            request,
            self.template_name,
            {
                'form': form,
            })

    def post(self, request):
        """
        POST request for processing the User account details form
        data passed from thesign up page and if
        form is valid saves user to database.
        """
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
    class base view to return a rendered
    tempate view of the user profile page
    """
    template_name = 'nannys_alternative/profile.html'


class EditProfile(TemplateView):
    """
    Class based view which renders the edit profile template with form
    which allows users to Edit their username,
    first name, last name, email address and a password with a password
    verifcation check.
    """
    template_name = 'nannys_alternative/edit_profile.html'

    def get(self, request, *args, **kwargs):
        """
        GET request for rendering the edit user profile
        page including the edit profile form
        """
        form = EditProfileForm()
        return render(
            request,
            self.template_name,
            {
                'form': form,
            })

    def post(self, request):
        """
        POST request for processing the edit profile form
        data passed from edit profile page and if
        form is valid updates and saves user data to database.
        """
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
    """
        Class based view to delete the selected
        user using the built in Django Deleteview.
    """
    model = User
    template_name = 'nannys_alternative/delete_profile.html'
    success_url = reverse_lazy('home')
