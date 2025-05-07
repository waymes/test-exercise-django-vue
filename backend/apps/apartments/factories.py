import factory
from .models import Apartment
from apps.users.factories import UserFactory

class ApartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Apartment

    name = factory.Faker('street_name')
    slug = factory.Sequence(lambda n: f"apartment-{n}")
    description = factory.Faker('sentence', nb_words=20)
    price = factory.Faker('pydecimal', left_digits=6, right_digits=2, positive=True)
    number_of_rooms = factory.Faker('random_int', min=1, max=6)
    square = factory.Faker('pydecimal', left_digits=4, right_digits=2, positive=True)
    availability = factory.Faker('boolean')
    owner = factory.SubFactory(UserFactory)

