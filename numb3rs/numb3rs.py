# Problem Set: https://cs50.harvard.edu/python/2022/psets/7/numb3rs/
""" 
Implement a function that expects an IPv4 address as input (str) and
returns True or False respectively, if that input is a valid IPv4 address or not.
Additionaly implement, in a test file, 2 or more functions that collectively test
the implementation of validate function thoroughly.
 """

import re

def validate(ip: str) -> bool:
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    # walrus operator
    if match := re.search(pattern, ip):
        group_1 = int(match.group(1)) 
        group_2 = int(match.group(2))
        group_3 = int(match.group(3))
        group_4 = int(match.group(4))
        # group loop
        groups = [group_1, group_2, group_3, group_4]
        for group in groups:
            if group >= 0 and group <= 255:
                continue
            else:
                return False
        return True
    else:
        return False

def main():
    print(validate(input("IPv4 Address: ")))

if __name__ == "__main__":
    main()