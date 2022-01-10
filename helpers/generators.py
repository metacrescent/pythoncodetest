import random
import string


def string_generator(size=8, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size)).upper()


def number_generator(size=8, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def alphanumerical_generator(size=8, chars=(string.digits + string.ascii_letters)):
    return ''.join(random.choice(chars) for _ in range(size))
