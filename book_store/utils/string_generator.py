import random
import string


def generated_email(chars=7):
    email = ''.join(random.choices(string.ascii_uppercase + string.digits, k=chars)) + '@fakemail.org'
    return email


def generated_password(chars=10):
    password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=chars))
    return password
