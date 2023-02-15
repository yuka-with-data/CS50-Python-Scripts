# import libraries
import random

# let user set a level 1, 2 or 3 (digits)
def get_level() -> int:
    while True:
        try:
            level = int(input("Level: "))
            if level in (1,2,3): 
                return(level)
            else:
                raise ValueError
        except ValueError:
            continue

# generate integers based on user input level
def generate_integer(level: int) -> int:
    # level check
    if level == 1:
        return random.randint(0,9) 
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)

def math_prob(level: int) -> int:
    score = 0
    for _ in range(10): 
        X, Y = generate_integer(level), generate_integer(level)
        for _ in range(3):
            answer_input = input(f"{X} + {Y} = ")
            if not answer_input.isdigit():
                print("EEE")
                continue
            if int(answer_input) == X + Y:
                score += 1
                break
            elif int(answer_input) != X + Y:
                print("EEE")
                continue
        else:
            # printing answer after 3 times attempt
            print(f"{X} + {Y} = {X+Y}")
    return score

# main function
def main():
    level = get_level()
    score = math_prob(level)
    print(f"Score: {score}")

if __name__ == "__main__":
    main()
