""" 
Run pytest to collectively test implementation of Jar 

 """
import pytest
from jar import Jar 

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar = Jar(100)
    assert jar.capacity == 100
    assert jar.size == 0

def test_str():
    # instanciate Jar
    jar = Jar() 
    assert str(jar) == ""
    # if n = 1
    jar.deposit(1)
    assert str(jar) == "🍪"
    # if n = 5
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(11)
    assert jar.size == 12
    try:
        jar.deposit(1)
    except ValueError:
        pass
    else:
        assert False, "ValueError not raised"
    assert jar.size == 12

def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    assert jar.size == 12
    jar.withdraw(6)
    assert jar.size == 6
    jar.withdraw(6)
    assert jar.size == 0
    try:
        jar.withdraw(2)
    except ValueError:
        pass
    else:
        assert False, "ValueError not raised"
    assert jar.size == 0