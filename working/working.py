# Problem Set: https://cs50.harvard.edu/python/2022/psets/7/working/
""" 
expects a str in either of the 12-hour formats 
and returns the corresponding str in 24-hour format 
 """

import re
import sys

def convert(s):
    try:
        hour_re = r"^([0-9]+):?([0-5][0-9])?\s*([A|P]M) to ([0-9]+)?:?([0-5][0-9])? ([A|P]M)"
        if match := re.search(hour_re, s):
            group_1, group_2, group_3, group_4, group_5, group_6 = int(match.group(1)),match.group(2),match.group(3),int(match.group(4)),match.group(5),match.group(6)
            # in case if there are no group_2 or/and group 5
            if group_2 == None:
                group_2 = 0
            if group_5 == None:
                group_5 = 0
            # convert groups to int
            group_2, group_5 = int(group_2), int(group_5)
            # if hours are more than 12
            if group_1 > 12 or group_4 > 12:
                raise ValueError
        else: 
            raise ValueError
    except:
        raise ValueError
    # if not 12 PM, then add 12
    if 'PM' in group_3 and group_1 != 12:
        group_1 += 12
    if 'PM' in group_6 and group_4 != 12:
        group_4 += 12
    # if 12 AM, then change to 0 AM
    if 'AM' in group_3 and group_1 == 12:
        group_1 = 0
    if 'AM' in group_6 and group_4 == 12:
        group_4 = 0

    return f"{group_1:02}:{group_2:02} to {group_4:02}:{group_5:02}"

def main():
    s = input("Hours: ")
    print(convert(s))

if __name__ == "__main__":
    main()
