from django.shortcuts import render, get_object_or_404, reverse, redirect
# from django.template.defaultfilters import slugify
# from django.views import generic, View
from django.views.generic import TemplateView
from .forms import UserAccountDetailsForm
from django.http import HttpResponseRedirect

"""
commented out above imports as may not e required - test and see tomorrow
"""


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


# class User_account_details():
#     template_name = 'nannys_alternative/user_account_details.html'



# class User_account_details(TemplateView):
#     template_name = 'nannys_alternative/user_account_details.html'
    
#     def post(self, request):

#         if request.method == 'POST':
#             form = UserAccountDetailsForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('home')

#         else:
#             form = UserAccountDetailsForm()
#             details = {
#                 'form': form,
#             }
#             return render(request, 'nannys_alternative/user_account_details.html', details)
    


"""

"""

class Sign_up(TemplateView):
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
            form.instance.user = request.user
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

"""
    # def post(self, request, *args, **kwargs):
    #     form = BookingForm(request.POST)
    #     booking = Booking.objects.all()
        
    #     if form.is_valid():
    #         form.instance.email = request.user.email
    #         email = form.instance.email
    #         form.instance.name = request.user.username
    #         name = form.instance.name
    #         form.instance.primary_guest = request.user
    #         primary_guest = form.instance.primary_guest
    #         number_of_guests = form.cleaned_data['number_of_guests']
    #         dietary_notes = form.cleaned_data['dietary_notes']
    #         Meal_time = form.cleaned_data['Meal_time']
    #         booking_date = form.cleaned_data['booking_date']
    #         additional_comments = form.cleaned_data['additional_comments']
    #         form.instance.slug = (f"{primary_guest}_{booking_date}_{Meal_time}")
    #         slug = form.instance.slug
    #         booked = form.save(commit=False)
    #         primary_guest = request.user
    #         booked.post = booked            
    #         booked.save() 
    #     else:
    #         form = BookingForm()
    #     return HttpResponseRedirect(reverse('bookings'))

