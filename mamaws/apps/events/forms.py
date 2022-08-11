from django import forms
from .models import Reservation

class ReservationCreationForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = (
            'party_name',
            'party_size',
            'party_date',
            'party_start_time',
            'party_end_time',
            'phone_number',
            'notes',
        )

	def __init__(self, *args, **kwargs):
		super(ReservationCreationForm, self).__init__(*args, **kwargs)
		# self.fields['shipping_address'].required = False
