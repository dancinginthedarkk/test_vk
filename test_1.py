import pytest

# tuple
test_tuple1 = (4, 5, 6, 7, 8)
test_tuple2 = [('abcdef', ('a', 'b', 'c', 'd', 'e', 'f')), ('test', ('t', 'e', 's', 't'))]


def test_type():
    assert type(test_tuple1) == tuple


@pytest.mark.parametrize('tup, x', test_tuple2)
def test_tuple(tup, x):
    result = tuple(x)
    assert x == result


def test_valid():
    result = (4, 5, 6, 7, 8, 9)
    try:
        test_tuple1.append(9)
        assert test_tuple1 == result
    except AttributeError:
        pass


# int
def test_int_type():
    a = 0
    assert type(a) == int


list_int = [([1, 2, 3, 0, -1], 3)]
@pytest.mark.parametrize('list_int, max_int', list_int)
def test_max_int(list_int, max_int):
    assert max(list_int) == max_int


def test_valid_int():
    result = 10
    try:
        a = 5 + '5'
        assert a == result
    except TypeError:
        pass

