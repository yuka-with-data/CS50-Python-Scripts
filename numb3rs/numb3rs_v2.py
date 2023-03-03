# Problem Set: https://cs50.harvard.edu/python/2022/psets/7/numb3rs/
""" 
Implement a function that expects an IPv4 address as input (str) and
returns True or False respectively, if that input is a valid IPv4 address or not.
Additionaly implement, in a test file, 2 or more functions that collectively test
the implementation of validate function thoroughly.
 """

import re
import pytest

def validate(ip: str) -> bool:
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    # walrus operator
    if match := re.search(pattern, ip):
        groups = [int(match.group(i)) for i in range(1,5)]
        return all(group in range(0, 256) for group in groups)
    else:
        return False

# pytest decorator
@pytest.mark.parametrize(
    "test_input,expected",
    [
        (r"1.2.3", False),
        (r"1.2.3.4", True),
        (r"1.2.3.4.5", False),
        (r"-10.3.2.1", False),
        (r"255.256.257.258", False),
        (r"255.255.255.255", True),
        (r"abc.def.ghi.jkl", False)
    ]
)
def test_validate(test_input, expected):
    assert validate(test_input) == expected


def main():
    print(validate(input("IPv4 Address: ")))

if __name__ == "__main__":
    main()