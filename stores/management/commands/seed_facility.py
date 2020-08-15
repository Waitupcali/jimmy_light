from django.core.management.base import BaseCommand
from stores.models import Facility


class Command(BaseCommand):

    help = "This command creates facilities."

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times",
    #         help="How many times do you want me to tell you that I love you?",
    #     )

    def handle(self, *args, **options):
        facilities = [
            "coupon",
            "air_con",
            "3rd_floor",
            "2nd_floor",
            "street_level",
            "location_on_map",
            "size_limits",
            "restroom",
            "restricted_space",
            "elevator",
            "wifi",
            "24/7_manned",
            "cctv",
            "separated_storage",
        ]

        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created!"))

