from django.views.generic import View
from django.shortcuts import render
from django_countries import countries
from django.core.paginator import Paginator
from django.http import HttpResponse
from . import models, forms


def all_stores(request):
    all_stores = models.Store.objects.all()
    return render(request, "stores/home.html", context={"stores": all_stores})


class SearchView(View):

    """ SearchView Definition """

    def get(self, request):

        country = request.GET.get("country")

        if country:

            form = forms.SearchForm(request.GET)

            if form.is_valid():

                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                store_type = form.cleaned_data.get("store_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                instant_book = form.cleaned_data.get("instant_book")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city is not None:
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if store_type is not None:
                    filter_args["store_type"] = store_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if instant_book is True:
                    filter_args["instant_book"] = True

                for facility in facilities:
                    filter_args["facilities"] = facility

                qs = models.Store.objects.filter(**filter_args).order_by("-created")

                paginator = Paginator(qs, 10, orphans=5)

                page = request.GET.get("page", 1)

                stores = paginator.get_page(page)

                return render(
                    request, "stores/search.html", {"form": form, "stores": stores}
                )

        else:

            form = forms.SearchForm()


        return render(request, "stores/search.html", {"form": form})
