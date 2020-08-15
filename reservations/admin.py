from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition """

    list_display = (
        "store",
        "status",
        "check_in",
        "check_out",
        "guest",
        "luggage_large_user",
        "luggage_medium_user",
        "luggage_small_user",
        "in_progress",
        "is_finished",
    )


    list_filter = ("status",)

    @admin.register(models.BookedDay)
    class BookedDayAdmin(admin.ModelAdmin):
        list_display = ("day", "reservation",)