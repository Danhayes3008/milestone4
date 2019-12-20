from django import forms
from .models import Donations

class MakePaymentForm(forms.Form):
    MONTH_CHOICE = [(i, i) for i in range(1, 12)]
    YEAR_CHOICE = [(i, i) for i in range(2017, 2036)]
    
    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label="Security code", required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICE, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICE, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
class DonationsForm(forms.ModelForm):
    class Meta:
        model = Donations
        fields = ('full_name', 'phone_number', 'country', 'postcode', 'town_or_city', 'streetadress1', 'streetaddress2', 'county')