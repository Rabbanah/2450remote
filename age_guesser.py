import random

def guess_age():
    # 1. Greet the user
    print("Hello! I'm a digital psychic, and I'm going to try to guess your age.")
    
    # 2. Ask for name
    name = input("First, what is your name? ")
    
    # Create a list of possible ages and shuffle them
    possible_ages = list(range(15, 31))
    random.shuffle(possible_ages)
    
    # 3. Guess ages loop
    for age in possible_ages:
        answer = input(f"Are you {age} years old? (y/n): ").lower()
        
        # 4. If the guess is right
        if answer == 'y':
            print(f"Hooray! I knew it! {name} is {age} years old.")
            return # This quits the function/program
            
        # 5. If the guess is wrong
        else:
            print("Rats.")
            
    print("Well, I've run out of guesses! You're harder to read than I thought.")

if __name__ == "__main__":
    guess_age()
