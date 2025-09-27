from django.core.exceptions import ValidationError
from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    @staticmethod
    def validate_age(age: int, error_to_raise):
        if age < 14:
            raise error_to_raise("We do not accept people who are under 14.")

    def clean(self):
        Musician.validate_age(self.age, ValidationError)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def is_adult(self) -> bool:
        return self.age >= 21
