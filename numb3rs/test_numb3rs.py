"""
Run pytest 
 """
# import module to pytest
from numb3rs import validate

# test_correct & assert
def test_correct():
    assert validate(r"1.10.33.211")
    assert validate(r"0.10.100.255")
    assert validate(r"125.0.0.1")
    assert validate(r"255.255.255.255")
    assert validate(r"0.0.0.0")

# test_incorrect & assert
def test_incorrect():
    assert not validate(r"0.0.0")
    assert not validate(r"1.2.3.4.5")
    assert not validate(r"256.0.0.1")
    assert not validate(r"1.256.333.444")
    assert not validate(r"256.256.256.256")
    assert not validate(r"yuka.with.data.python")
    
# call main()
def main():
    test_correct()
    test_incorrect()

# __name__
if __name__ == "__main__":
    main()