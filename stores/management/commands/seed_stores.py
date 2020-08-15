import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users import models as users_models
from stores import models as stores_models


class Command(BaseCommand):

    help = "This command creates stores."

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many stores do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = users_models.User.objects.all()
        store_types = stores_models.StoreType.objects.all()
        seeder.add_entity(
            stores_models.Store,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "store_type": lambda x: random.choice(store_types),
                "price": lambda x: random.randint(3000, 5000),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        facilities = stores_models.Facility.objects.all()

        for pk in created_clean:
            store = stores_models.Store.objects.get(pk=pk)
            for i in range(3, random.randint(10, 30)):
                stores_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    store=store,
                    file=f"store_photos/{random.randint(1, 31)}.webp",
                )


            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    store.facilities.add(f)


        self.stdout.write(self.style.SUCCESS(f"{number} stores created!"))
