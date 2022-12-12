from django import forms


BOOKING_COUNT_CHOICES = [(i, str(i)) for i in range(1, 6)]

class CartAddBookingForm(forms.Form):
    booking_count = forms.TypedChoiceField(
        choices = BOOKING_COUNT_CHOICES,
        coerce  = int
    )
    
    update = forms.BooleanField(
        required = False,
        initial  = False,
        widget   = forms.HiddenInput
    )