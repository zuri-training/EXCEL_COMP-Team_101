from django.core.exceptions import ValidationError


def file_size_limiter(value):
    limit = 5 * 1024 * 1024
    file_size = value.size

    if file_size > limit:
        raise ValidationError('File too large. Size should not exceed 5 MiB.')
    else:
        return value
