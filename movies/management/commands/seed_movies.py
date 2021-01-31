from random import choice, randint
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from movies.models import Movie
from categories.models import Category
from people.models import Person


class Command(BaseCommand):

    help = "This command seeds movies"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total", help="How many movies do you want to create?", default=10
        )

    def handle(self, *args, **options):
        total = int(options.get("total"))
        categories = Category.objects.all()
        directors = Person.objects.filter(kind=Person.KIND_DIRECTOR)
        seeder = Seed.seeder()
        seeder.add_entity(
            Movie,
            total,
            {
                "title": lambda x: seeder.faker.city(),
                "year": lambda x: seeder.faker.year(),
                "rating": lambda x: randint(1, 5),
                "category": lambda x: choice(categories),
                "cover_image": lambda x: f"movies/{randint(1,25)}.jpg",
                "director": lambda x: choice(directors),
            },
        )
        created = seeder.execute()
        clean = flatten(list(created.values()))
        people = Person.objects.filter(kind=Person.KIND_ACTOR)
        for pk in clean:
            movie = Movie.objects.get(pk=pk)
            for actor in people:
                magic_number = randint(0, 15)
                if magic_number % 2 == 0:
                    movie.cast.add(actor)

        self.stdout.write(self.style.SUCCESS(f"{total} movies created!"))
