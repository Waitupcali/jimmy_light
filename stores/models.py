from django.db import models
from core import models as core_models
from users import models as user_models
from django.utils import timezone
from django_countries.fields import CountryField


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class StoreType(AbstractItem):

    """ StoreType Model Definition """

    class Meta:
        verbose_name = "Store Type"
        ordering = ["name"]

class Facility(AbstractItem):

    """ Facility Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"

class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """
    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="store_photos")
    store = models.ForeignKey("Store", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

class Store(core_models.TimeStampedModel):

    """ Store Model definition """

    name = models.CharField(max_length=140)
    discription = models.TextField()
    country = CountryField(default="South of Korea")
    city = models.CharField(max_length=80)
    section = models.CharField(max_length=80)    
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    luggage_large_store = models.IntegerField(help_text="size: confirmed later", default=3)
    luggage_medium_store = models.IntegerField(help_text="size: confirmed later", default=3)
    luggage_small_store = models.IntegerField(help_text="size: confirmed later", default=3)

    opening_mon = models.TimeField(blank=True, default=timezone.now)
    opening_wen = models.TimeField(blank=True, default=timezone.now)
    opening_thu = models.TimeField(blank=True, default=timezone.now)
    opening_fri = models.TimeField(blank=True, default=timezone.now)
    opening_tue = models.TimeField(blank=True, default=timezone.now)
    opening_sat = models.TimeField(blank=True, default=timezone.now)
    opening_sun = models.TimeField(blank=True, default=timezone.now)

    closing_mon = models.TimeField(blank=True, default=timezone.now)
    closing_tue = models.TimeField(blank=True, default=timezone.now)
    closing_wen = models.TimeField(blank=True, default=timezone.now)
    closing_thu = models.TimeField(blank=True, default=timezone.now)
    closing_fri = models.TimeField(blank=True, default=timezone.now)
    closing_sat = models.TimeField(blank=True, default=timezone.now)
    closing_sun = models.TimeField(blank=True, default=timezone.now)

    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="stores", on_delete=models.CASCADE, blank=True
    )
    store_type = models.ForeignKey("StoreType", related_name="stores", on_delete=models.SET_NULL, null=True, blank=True)
    facilities = models.ManyToManyField("Facility", related_name="stores", blank=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0

        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()

            return round(all_ratings / len(all_reviews))

        return 0