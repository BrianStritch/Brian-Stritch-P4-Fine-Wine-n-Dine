#### __pakages to be installed__
 - pip3 install Django==3.2 gunicorn
 - pip3 install dj_database_url psycopg2
 - pip3 install dj3-cloudinary-storage
 - pip3 freeze -- local > requirements.txt
 - django-admin startproject codestar .  this is the code to create the new django project
 - python3 manage.py startapp bookings
 - python3 manage.py startapp reviews

 - python3 manage.py migrate   this migrates all our changes to the DB

 - python3 manage.py runserver    this is the code to run the file

 after creating database models you can make your migrations
 - python3 manage.py makemigrations
 then 
 - python3 manage.py migrate












# __datetimepicker__


    - https://nancylin.xyz/how-to-implement-date-time-picker-in-django-without-javascript/


You are here: Home / Software Development / How to Implement Date & Time Picker in Django without Javascript
How to Implement Date & Time Picker in Django without Javascript
Published On July 26, 2021, Last Updated On July 25, 2021 by Nancy Lin

Date picker and time picker are a must when you are developing a professional Django application. Using it has 2 main advantages:

Guarantees that the user will enter the data in the correct format
Easy to user interface
Date Picker is usually implemented with Javascript in Django, but HTML5 actually comes with a date picker element that can be implemented onto Django forms making it ultra light weight.

1. Create widget.py
We will be creating the date picker as custom widgets in Django. Widgets can be created directly in forms.py. But, I find that it is easier to organize and maintain down the road if they are in a separate widgets.py file.

Widget.py is created in the project folder with forms.py, models.py, etc.

2. Create the Widget
There are 3 possible pickers to choose from:

Date Picker
Time Picker (only a controlled input element, no actual graphic selection)
Date Time Picker
This is an example of the code in widget.py


    from django import forms

    class DatePickerInput(forms.DateInput):
        input_type = 'date'

    class TimePickerInput(forms.TimeInput):
        input_type = 'time'

    class DateTimePickerInput(forms.DateTimeInput):
        input_type = 'datetime'
The class can have any name, and they inherit from their respective Inputs. Because it is HTML5 element instead of Javascript, all you need to do to initiate it is by declaring the input_type.

3. Using the Widgets in Django Form
Now that we created the widgets, we move to forms.py and import the widgets we just created.

We can use the widgets in Form or ModelForm.

In Form

    from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput

    class ExampleForm(forms.Form):
        my_date_field = forms.DateField(widget=DatePickerInput)
        my_time_field = forms.TimeField(widget=TimePickerInput)
        my_date_time_field = forms.DateTimeField(widget=DateTimePickerInput)
In ModelForm

from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput

class ExampleForm(ModelForm):
    class Meta:
        model = Example
        fields = ['my_date_field', 'my_time_field', 'my_date_time_field']

        widgets = {
            'my_date_field' : DatePickerInput(),
            'my_time_field' : TimePickerInput(),
            'my_date_time_field'' : DateTimePickerInput(),
        }
