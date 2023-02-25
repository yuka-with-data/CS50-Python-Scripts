import sys

def command_line_check(): # lines.py hello.py
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

def read_count() -> int:
    try:
        count_lines = 0
        with open(sys.argv[1],"r") as file:
            for line in file:
                line = line.lstrip()
                # check comments and empty lines
                if len(line) == 0 or line.startswith("#"):
                    continue
                count_lines += 1
        return count_lines
    except FileNotFoundError:
        sys.exit("File does not exist")

def main():
    command_line_check()
    count = read_count()
    print(count)

if __name__ == "__main__":
    main()