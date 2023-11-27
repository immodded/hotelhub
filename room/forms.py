from django import forms

class BookingForm(forms.Form):
    guest_name = forms.CharField(max_length=100, label='Guest Name')
    check_in_date = forms.DateField(label='Check-in Date')
    check_out_date = forms.DateField(label='Check-out Date')

    def clean(self):
        cleaned_data = super().clean()
        check_in_date = cleaned_data.get('check_in_date')
        check_out_date = cleaned_data.get('check_out_date')

        if check_in_date and check_out_date and check_out_date <= check_in_date:
            raise forms.ValidationError("Check-out date must be after check-in date")
