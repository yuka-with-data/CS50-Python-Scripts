# Problem Set: https://cs50.harvard.edu/python/2022/psets/6/scourgify/
""" 
Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name. 
Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the first cannot be read, 
the program should exit via sys.exit with an error message.
 """

import sys
import csv

def check_command_line_arg(): 
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # check if CSV files
    if ".csv" not in sys.argv[1] and ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")

def read_file():
    dict_output = []
    try:
        with open(sys.argv[1],"r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(", ")
                house = row["house"]
                dict_output.append({"first": first, "last": last, "house": house})
            return dict_output
    except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")

def write_file(dict_output):
    with open(sys.argv[2], "w") as file2:
        writer = csv.DictWriter(file2, fieldnames=["first","last","house"], lineterminator='\n')
        writer.writeheader()
        for row in dict_output:
            writer.writerow(row)

def main():
    check_command_line_arg()
    dict_output = read_file()
    write_file(dict_output)

if __name__ == "__main__":
    main()