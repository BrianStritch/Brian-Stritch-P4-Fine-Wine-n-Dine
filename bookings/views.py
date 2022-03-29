from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.views.generic import TemplateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import BookingForm
from .models import Booking
from .bscode import reverseMealDate
from datetime import datetime


class Bookings(TemplateView):   

    def get(self, request):
        bookings = Booking.objects.all()
        template_name = 'bookings/bookings.html'
        paginate_by = 8
        return render(
            request, 
            template_name,
            {
                'bookings': bookings,
            })       


class CreateBookings(TemplateView):
    template_name = 'bookings/create_a_booking.html'
    booking = Booking.objects.all()
    bookings_list = {
        'bookings': booking,
    }

    def get(self, request):
        form = BookingForm()
        booking = Booking.objects.all()
        bookings_list = {
            'bookings':booking,
        }
        return render(
            request, 
            self.template_name, 
            {
            'form': form,                
            })

    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        booking = Booking.objects.all()       

        
        if form.is_valid():
            form.instance.primary_guest = request.user
            primary_guest = form.instance.primary_guest
            number_of_guests = form.cleaned_data['number_of_guests']
            dietary_notes = form.cleaned_data['dietary_notes']
            Meal_time = form.cleaned_data['Meal_time']            
            booking_date = form.cleaned_data['booking_date']
            additional_comments = form.cleaned_data['additional_comments']
            form.instance.slug = (f"{primary_guest}_{booking_date}_{Meal_time}")
            slug = form.instance.slug

            already = Booking.objects.filter(
                primary_guest=primary_guest,
                Meal_time=Meal_time, 
                booking_date__contains=booking_date
                )  
            q = Booking.objects.filter(
                Meal_time=Meal_time, 
                booking_date__contains=booking_date
                )        
            check = q.count()  

            if not already:
                if check < 6:
                    booked = form.save(commit=False)
                    primary_guest = request.user
                    booked.post = booked            
                    booked.save()
                    return HttpResponseRedirect(reverse('bookings'))

                else:
                    message = 'Unfortunately we are fully booked for your \
                        chosen mealtime, please choose another mealtime.'
                    return render(
                    request, 
                    self.template_name, 
                    {
                    'form': form,
                    'message': message,              
                    })
            else:
                message = 'You currently have a booking at this time, \
                    please choose another timeslot.'
                return render(
                    request, 
                    self.template_name, 
                    {
                    'form': form,
                    'message': message,               
                    })

        else:
            form = BookingForm()
        return HttpResponseRedirect(reverse('bookings'))


class EditBookings(View):
    template_name = 'bookings/edit_booking.html'

    def get(self, request, pk, *args, **kwargs):
        queryset = Booking.objects.all()
        booking = get_object_or_404(queryset, id=pk)
        form = BookingForm(instance=booking)
        return render(
            request, 
            self.template_name, 
            {
            'form': form,              
            })

    def post(self, request, pk, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        queryset = Booking.objects.all()
        booking = get_object_or_404(queryset, id=pk)
        form = BookingForm(request.POST, instance=booking)
        

        if form.is_valid():            
            Meal_time = form.cleaned_data['Meal_time']
            booking_date = form.cleaned_data['booking_date']
            form.instance.primary_guest = request.user
            primary_guest = form.instance.primary_guest

            already = Booking.objects.filter(
                primary_guest=primary_guest,
                Meal_time=Meal_time,
                booking_date__contains=booking_date
                )    
            q = Booking.objects.filter(
                Meal_time=Meal_time,
                booking_date__contains=booking_date
                )
            check = q.count()

            if not already:
                if check < 6:
                    booked = form.save(commit=False)
                    booked.post = booked            
                    booked.save()
                    return HttpResponseRedirect(reverse('bookings'))
                                
                else:
                    message = 'Unfortunately we are fully booked for your\
                         chosen mealtime, please choose another mealtime.'
                    return render(
                        request, 
                        self.template_name, 
                        {
                        'form': form,
                        'message': message,               
                        })
            else:
                message = 'You currently have a booking at this time, \
                    please choose another timeslot.'
                return render(
                    request, 
                    self.template_name,
                    {
                        'form': form,
                        'message': message,
                    })
        else:
            form = BookingForm()
            return HttpResponseRedirect(reverse('bookings'))



class BookingDetails(View):

    def get(self, request, slug , *args, **kwargs):
        queryset = Booking.objects.all()
        booking = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "bookings/bookings_detail.html",
            {
                'booking': booking, 
            },
        )


class DeleteBooking(DeleteView):
    model = Booking
    template_name = 'bookings/delete_booking.html'
    success_url = reverse_lazy('bookings')


class AdminBookings(TemplateView):
    template_name = 'bookings/admin_bookings_view.html'

    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.all().order_by('booking_date')
        
        return render(request,
            'bookings/admin_bookings_view.html',
            {
                'bookings': bookings,
            }
        )