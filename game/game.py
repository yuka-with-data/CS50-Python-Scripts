# Problem Set: https://cs50.harvard.edu/python/2022/psets/4/game/
""" 
Prompts the user for a level, n.
If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and n, inclusive, using the random module.
Prompts the user to guess that integer. 
If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
 """

import random

def main():
    l = level()
    guess(l)

# 1st loop to ask user a level of the game
def level() -> int:
    while True:
        try:
            # user input of game level
            level_input = int(input("Level: "))
            # randomly pick int between 1 and level_input
            random_int = random.randint(1, level_input)
            # print(random_int) # debug print
            return random_int
        except ValueError:
            continue

# 2nd loop to ask user a guess
def guess(random_int):
    while True:
        try:
            # user input of guess
            guess_input = int(input("Guess: "))
            # Conditions
            if guess_input > random_int:
                print("Too large!")
                continue
            elif guess_input < random_int:
                print("Too small!")
                continue
            else:
                print("Just right!")
                break
        except ValueError:
            continue

if __name__ == "__main__":
    main()