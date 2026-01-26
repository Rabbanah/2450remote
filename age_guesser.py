import random

def guess_age():
    print("Hello! I'm a digital psychic, and I'm going to try to guess your age.")
    
    name = input("First, what is your name? ")
    lowest = 15
    highest = 100
    
    age = random.randint(lowest, highest)
    
    answered_correctly = False
    while not answered_correctly:
        print(f"\nMy psychic senses suggest you are... {age}?")
        feedback = input("Am I right? (y), or am I too low (l), or too high (h)? ").lower()

        if feedback == 'y':
            answered_correctly = True
        elif feedback == 'h':
            highest = age - 1
            if lowest > highest:
                print("Wait... something doesn't add up. Are you tricking the psychic?")
                break
            age = random.randint(lowest, highest)
        elif feedback == 'l':
            lowest = age + 1
            if lowest > highest:
                print("Hmm, the spirits are confused. Your answers are contradicting each other!")
                break
            age = random.randint(lowest, highest)
        else:
            print("Please enter 'y', 'l', or 'h'.")

    if answered_correctly:
        print(f"\nHooray! I knew it! {name} is {age} years old.")

if __name__ == "__main__":
    guess_age()
