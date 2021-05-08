from django.core.exceptions import ValidationError
def validate_patnof(value):
    if len(str(value)) !=8 and  len(str(value)) !=11:
        raise  ValidationError("Need to be 8 or 11 in length")
    else:
        return value