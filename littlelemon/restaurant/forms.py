from django.forms import ModelForm


from .models import Booking


class Bookingform(ModelForm): 
    class Meta: 
        model = Booking 
        fields = ['id', 'First_name', 'Last_name', 'Guess_number', 'Comments']