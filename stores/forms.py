from django import forms
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):

    city = forms.CharField(required=False)
    country = CountryField(default="KR").formfield()
    store_type = forms.ModelChoiceField(
        required=False, empty_label="Any Kind", queryset=models.StoreType.objects.all()
    )
    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    facilities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
