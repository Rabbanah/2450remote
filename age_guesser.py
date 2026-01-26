import random

def guess_age():
    print("Hello! I'm a digital psychic, and I'm going to try to guess your age.")
    
    name = input("First, what is your name? ")
    lowest = 15
    highest = 100
    possible_ages = list(range(lowest, highest))
    shuff = random.shuffle(possible_ages)
    age = shuff[0]
    
    answer = 'n'
    while answer != 'y':
        change = input(f"Are you older or younger than {age}? (o/y): ").lower()
        if change == 'o':
            possible_ages = list(range(age, highest))
            youngest = age
            shuff = random.shuffle(possible_ages)
            age = shuff[0]
            answer = input(f"Are you {age} years old? (y/n): ").lower()
        elif change == 'y':
            possible_ages = list(range(lowest, age))
            highest = age
            shuff = random.shuffle(possible_ages)
            age = shuff[0]
            answer = input(f"Are you {age} years old? (y/n): ").lower()

    if answer == 'y':
        print(f"Hooray! I knew it! {name} is {age} years old.")
        return

if __name__ == "__main__":
    guess_age()
