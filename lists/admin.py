from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "user",
        "count_store",
    )

    filter_horizontal = (
        "stores",
    )

    search_fields = ("^name",)
    