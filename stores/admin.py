from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.StoreType, models.Facility)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.stores.count()


# StackedInline is different form of the inline admin
class PhotoInline(admin.TabularInline):

    model = models.Photo

@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):

    """ Store Admin Definition """

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Bacis Info",
            {"fields": ("name", "discription", "city", "section", "address",)},
        ),

        (
            "Price Option",
            {"fields": ("price",)}

        ),

        (
            "Luggage Option",
            {"fields":("luggage_large_store", "luggage_medium_store", "luggage_small_store",)},
        ),

        (
            "Tiems for User",
            {   
                # "classes": ("collapse",),
                "fields": ("check_in", "check_out", "instant_book",)},
        ),

        (
            "Times for Store",
            {
                "classes": ("collapse",),
                "fields":
                    (
                    "opening_mon", "opening_wen", "opening_thu", "opening_fri", "opening_tue", "opening_sat",
                    "opening_sun", "closing_mon", "closing_tue", "closing_wen", "closing_thu","closing_sat",
                    "closing_sun",)},
        ),

        (
            "More About the Space",
            {
                "fields": ("facilities",),
            },
        ),

        (
            "Last Details", 
            {"fields": ("host",)},
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "section",
        "price",
        "address",
        "host",
        "check_in",
        "check_out",
        "instant_book",
        "count_facilities",
        "count_photos",
        "total_rating",
    )

    ordering = (
        "name",
        "price",
    )

    list_filter = (
        "instant_book",
        "store_type",
        "facilities",
        "city",
        "section",
    )

    raw_id_fields = ("host",)

    search_fields = (
        "^city",
        "^host__username",
    )

    filter_horizontal = (
        "facilities",
    )

    def count_facilities(self, obj):
        return obj.facilities.count()
        
    count_facilities.short_description = "count_facilities"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo counts"

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Tumbnail"
