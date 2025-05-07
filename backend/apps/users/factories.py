import factory
from .models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence(lambda n: f'user{n}@example.com')
    is_verified = True
    is_superuser = True
    is_active = True
    password = factory.PostGenerationMethodCall('set_password', 'password123')
