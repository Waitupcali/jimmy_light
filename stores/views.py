import os
import requests
from django.views.generic import View
from django.utils.http import urlencode
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from . import models, forms


def all_stores(request):
    all_stores = models.Store.objects.all()
    return render(request, "stores/home.html", context={"all_stores": all_stores})


class SearchView(View):

    """ SearchView Definition """

    def get(self, request):

        city = request.GET.get("city")

        if city:

            form = forms.SearchForm(request.GET)

            if form.is_valid():

                qs = models.Store.objects.all().order_by("-created")
                paginator = Paginator(qs, 20, orphans=5)
                page = request.GET.get("page", 1)
                stores_result = paginator.get_page(page)

                #To get the city's location
                def extract_lat_lng(address_or_postalcode, data_type = 'json'):
                    api_key = os.environ.get("API_ID")
                    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
                    params = {"address":address_or_postalcode, "key":api_key}
                    url_params = urlencode(params)
                    url = f"{endpoint}?{url_params}"
                    r = requests.get(url)
                    if r.status_code not in range(200, 299):
                        return {}
                    latlng = {}
                    try:
                        latlng = r.json()['results'][0]['geometry']['location']
                        city_lat = latlng.get("lat")
                        city_lng = latlng.get("lng")
                    except:
                        return {}
                    return city_lat, city_lng

                location = extract_lat_lng(city)

            return render(
                    request, "stores/search.html", {"form": form, "stores_result": stores_result, "city":city, "location":location}
                )

        else:

            form = forms.SearchForm()
            all_stores = models.Store.objects.all()
            
        return render(request, "stores/search.html", {"form": form, "all_stores": all_stores,})
