import random

def guess_age():
    print("Hello! I'm a digital psychic, and I'm going to try to guess your age.")
    
    name = input("First, what is your name? ")
    
    possible_ages = list(range(15, 31))
    random.shuffle(possible_ages)
    
    for age in possible_ages:
        answer = input(f"Are you {age} years old? (y/n): ").lower()
        
        if answer == 'y':
            print(f"Hooray! I knew it! {name} is {age} years old.")
            return

        if answer == 'n':
            change = input(f"Are you older or younger than {age}? (o/y): ").lower()
            if
            
        else:
            print("Rats.")
            
    print("Well, I've run out of guesses! You're harder to read than I thought.")

if __name__ == "__main__":
    guess_age()
