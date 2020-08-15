import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from reservations import models as reservation_models
from users import models as user_models
from stores import models as store_models

NAME = "reservations"


class Command(BaseCommand):

    help = f"This command creates {NAME}."

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int7
            help="How many reviews do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        stores = store_models.Store.objects.all()
        seeder.add_entity(
            reservation_models.Reservation, number, {

                "status": lambda x: random.choice([
                        "pending",
                        "confirmed",
                        "canceled",
                        ]),
                "luggage_large_user": lambda x: random.randint(1, 3),
                "luggage_medium_user": lambda x: random.randint(1, 3),
                "luggage_small_user": lambda x: random.randint(1, 3),
                "guest": lambda x: random.choice(users),
                "store": lambda x: random.choice(stores),
                "check_in": lambda x: datetime.now()
                - timedelta(days=random.randint(3, 25)),
                "check_out": lambda x: datetime.now() 
                + timedelta(days=random.randint(3, 25)),

            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))

