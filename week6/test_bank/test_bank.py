from bank import value

def test_value_100():
    assert value("whats up") == 100
    assert value("yo!") == 100

def test_value_20():
    assert value("Hey!") == 20
    assert value("how is you?") == 20

def test_value_100():
    assert value("Hello") == 0
    assert value("hello") == 0
