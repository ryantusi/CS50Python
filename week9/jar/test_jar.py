from jar import Jar

def test_init():
    cookie1 = Jar()
    assert cookie1.capacity == 12
    cookie2 = Jar(10)
    assert cookie2.capacity == 10

def test_str():
    cookie = Jar(10)
    assert str(cookie) == ""
    cookie.deposit(5)
    assert str(cookie) == "🍪🍪🍪🍪🍪"
    cookie.withdraw(2)
    assert str(cookie) == "🍪🍪🍪"

def test_deposit():
    cookie3 = Jar()
    cookie3.deposit(3)
    cookie3.deposit(2)
    assert cookie3.size == 5

def test_withdraw():
    cookie4 = Jar()
    cookie4.deposit(10)
    cookie4.withdraw(3)
    assert cookie4.size == 7
