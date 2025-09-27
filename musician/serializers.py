from rest_framework import serializers
from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = (
            "id",
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying",
            "is_adult"
        )

    def validate_age(self, value):
        Musician.validate_age(value, serializers.ValidationError)
        return value
