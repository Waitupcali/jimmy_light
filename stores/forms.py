from django import forms
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):

    # country = CountryField(default="KR", required=False).formfield()
    city = forms.CharField(required=False)
    check_in = forms.DateTimeField(required=False)
    
    store_type = forms.ModelChoiceField(
        required=False, empty_label="Any Kind", queryset=models.StoreType.objects.all()
    )
    facilities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
