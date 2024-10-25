from main import Root


def test_1():
    assert Root.get_root(25) == 5


def test_2():
    assert type(Root.get_root(12)) is int


def test_3():
    assert type(Root.get_root(12.5)) is int

