from functools import partial


def power(base, exponent):
    return base**exponent


square = partial(power, exponent=2)


def test_partials():
    assert square(2) == 4
