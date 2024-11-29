import re
from django.forms import ModelForm, ValidationError, DateInput
from .models import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['phone_number', 'booking_date', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Phone'})
        # self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        # self.fields['number_of_adults'].widget.attrs.update({'class': 'form-select', 'aria-label': 'Adult'})
        self.fields['booking_date'].widget.attrs.update({'class': 'input-field check-in', 'placeholder': 'dd-mm-yy',
                                                         'type': 'date'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Message', 'rows': 3})

    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data.get('phone_number')
    #     if not re.match(r'^\+998\d{9}$', phone_number):
    #         raise ValidationError('Please enter a valid Uzbekistan phone number. Example: +998XXXXXXXXX')
    #     return phone_number
