# Problem Set: https://cs50.harvard.edu/python/2022/psets/7/watch/

""" 
Implement a function caled parse that expects a string of HTML as input, 
extracts any YouTube URL that's the value of a src attribute of an iframe element
and returns its shorter, shareable youtu.be equivalent as a str. 
Expect that any such URL will be in one of the formats below.
http://youtube.com/embed/xvFZjo5PgG0
https://youtube.com/embed/xvFZjo5PgG0
https://www.youtube.com/embed/xvFZjo5PgG0
Assume that the value of src will be surrounded by double quotes. 
Assume that the input will contain no more than one such URL.
If the input does not contain any such URL at all, return None. 

 """
import re
import sys

def parse(s: str):
    if re.search(r"<iframe(.)*?</iframe>", s):
        if match := re.search(r"(http)(s)*?:\/\/(www\.)*?youtube\.com\/embed\/([a-z_A-Z_0-9_]+)", s):
            attr = match.group(4)
            return "https://youtu.be/" + attr

def main():
    print(parse(input("HTML: ")))

if __name__ == "__main__":
    main()