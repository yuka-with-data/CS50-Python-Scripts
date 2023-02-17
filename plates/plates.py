def main():
    plate = input("PLATE: ").strip().upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s: str) -> bool:
    if len(s) < 2 or len(s) > 6:
        print("invalid length")
        return False

    resort = []
    for char in s[:2]:
        resort.append(char.isalpha())
    if not all(resort):
        print("Doesn't start with 2 Chars")
        return False

    for i in range(0,len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                print("First Num can't be 0")
                return False
            else:
                break

    for i, char in enumerate(s):
        if char.isdigit():
            if not s[i:].isdigit():
                print("Digits are in the middle")
                return False 

    punct = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
    for char in s:
        if char in punct:
            print("Punctuation Error")
            return False

    return True

if __name__ == "__main__":
    main()

