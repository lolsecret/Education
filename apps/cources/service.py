from django.core.exceptions import ValidationError


def validate_round_hour(value):
    if not value.minute == value.second == value.microsecond == 0:
        raise ValidationError(
            'This should be a round hour.',
            params={'value': value},
        )