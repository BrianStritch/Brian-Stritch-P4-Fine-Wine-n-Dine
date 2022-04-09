"""
    imports  ------Bookings views.py----------------------
"""
# third party imports
from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.views.generic import TemplateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
# internal imports
from .forms import BookingForm
from .models import Booking


class Bookings(TemplateView):
    """
        Class based view to display bookings
        relative to the logged in user
    """
    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.all().order_by('booking_date')
        template_name = 'bookings/bookings.html'
        paginate_by = 6
        return render(
            request,
            template_name,
            {
                'bookings': bookings,
            })


class CreateBookings(TemplateView):
    """
        Class based view to render create bookings page
        with BookingForm to create new bookings, GET request
        data from user and process POST request accordingly
    """
    template_name = 'bookings/create_a_booking.html'
    booking = Booking.objects.all()
    bookings_list = {
        'bookings': booking,
    }

    def get(self, request, *args, **kwargs):
        """
        GET request for rendering the create booking
        page including the bookingform
        """
        form = BookingForm()
        booking = Booking.objects.all()
        bookings_list = {
            'bookings': booking,
        }
        return render(
            request,
            self.template_name,
            {
                'form': form,
            })

    def post(self, request):
        """
        POST request for processing the bookingform
        data passed from the create booking form and if
        form is valid and if specific conditions are met
        saves booking to database.
        """
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
            form.instance.slug = (
               f"{primary_guest}_{booking_date}_{Meal_time}"
               )
            slug = form.instance.slug

            already_booked = Booking.objects.filter(
                primary_guest=primary_guest,
                Meal_time=Meal_time,
                booking_date__contains=booking_date
                )
            query = Booking.objects.filter(
                Meal_time=Meal_time,
                booking_date__contains=booking_date
                )
            check = query.count()

            if not already_booked:
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
    """
        Class based view to display edit booking
        page with booking form relative to the
        current selected booking and processing the
        POST data and saving updated data to the database.
    """
    template_name = 'bookings/edit_booking.html'

    def get(self, request, pk):
        """
        GET request to render the edit bookings page relative to
        the selected booking with the attached Booking form
        """
        queryset = Booking.objects.all()
        booking = get_object_or_404(queryset, id=pk)
        form = BookingForm(instance=booking)
        return render(
            request,
            self.template_name,
            {
                'form': form,
            })

    def post(self, request, pk):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid, meets the specified
        requirements and updates the data accordingly, or returns to the
        edit booking view displaying the error message.
        """
        queryset = Booking.objects.all()
        booking = get_object_or_404(queryset, id=pk)
        form = BookingForm(request.POST, instance=booking)

        if form.is_valid():
            Meal_time = form.cleaned_data['Meal_time']
            booking_date = form.cleaned_data['booking_date']
            form.instance.primary_guest = request.user
            primary_guest = form.instance.primary_guest

            already_booked = Booking.objects.filter(
                primary_guest=primary_guest,
                Meal_time=Meal_time,
                booking_date__contains=booking_date
                )
            query = Booking.objects.filter(
                Meal_time=Meal_time,
                booking_date__contains=booking_date
                )
            check = query.count()

            if not already_booked:
                if check < 6:
                    booked = form.save(commit=False)
                    booked.post = booked
                    booked.save()
                    return HttpResponseRedirect(reverse('bookings'))

                else:
                    message = 'Unfortunately we are fully booked for your\
                         chosen mealtime, please choose another mealtime'
                    return render(
                        request,
                        self.template_name,
                        {
                            'form': form,
                            'message': message,
                        })
            else:
                message = 'You currently have a booking at this time, \
                    please choose another timeslot'
                return render(
                    request,
                    self.template_name,
                    {
                        'form': form,
                        'message': message,
                    })
        else:
            form = BookingForm()
            return render(
                request,
                self.template_name,
                {
                    'form': form,
                })


class BookingDetails(View):
    """
        Class based view to display the selected
        bookings specific details.
    """
    def get(self, request, slug):
        """
        class based function to render the bookings detail page
        diaplaying the booking details for the selected booking
        """
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
    """
        Class based view to delete the selected
        booking using the built in Django Deleteview.
    """
    model = Booking
    template_name = 'bookings/delete_booking.html'
    success_url = reverse_lazy('bookings')


class AdminBookings(TemplateView):
    """
        Class based view to render the Admin bookings page
        and display all bookings in a table to the administrator.
    """
    template_name = 'bookings/admin_bookings_view.html'

    def get(self, request, *args, **kwargs):
        """
        GET request to render the admin bookings view and diaply all bookings
        """
        bookings = Booking.objects.all().order_by('booking_date')

        return render(
            request,
            'bookings/admin_bookings_view.html',
            {
                'bookings': bookings,
            }
        )


class AdminBookingsApproved(TemplateView):
    """
        Class based view to render the Admin bookings page
        and display all bookings in a table to the administrator.
    """
    template_name = 'bookings/admin_bookings_view_approved.html'

    def get(self, request, *args, **kwargs):
        """
        GET request to render the admin bookings view and diaply all bookings
        """
        bookings = Booking.objects.all().order_by('booking_date')

        return render(
            request,
            'bookings/admin_bookings_view_approved.html',
            {
                'bookings': bookings,
            }
        )


class AdminBookingsPending(TemplateView):
    """
        Class based view to render the Admin bookings page
        and display all bookings in a table to the administrator.
    """
    template_name = 'bookings/admin_bookings_view_pending.html'

    def get(self, request, *args, **kwargs):
        """
        GET request to render the admin bookings view and diaply all bookings
        """
        bookings = Booking.objects.all().order_by('booking_date')

        return render(
            request,
            'bookings/admin_bookings_view_pending.html',
            {
                'bookings': bookings,
            }
        )


class AdminBookingsCompleted(TemplateView):
    """
        Class based view to render the Admin bookings page
        and display all bookings in a table to the administrator.
    """
    template_name = 'bookings/admin_bookings_view_completed.html'

    def get(self, request, *args, **kwargs):
        """
        GET request to render the admin bookings view and diaply all bookings
        """
        bookings = Booking.objects.all().order_by('booking_date')

        return render(
            request,
            'bookings/admin_bookings_view_completed.html',
            {
                'bookings': bookings,
            }
        )
