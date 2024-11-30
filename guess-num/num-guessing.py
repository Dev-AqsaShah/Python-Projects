import random

def main():
    # Generate a random number between 0 and 99
    secret_number = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99...")
    
    while True:
        # Prompt the user to enter a guess
        try:
            guess = int(input("Enter a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Check if the guess is correct, too high, or too low
        if guess > secret_number:
            print("Your guess is too high")
        elif guess < secret_number:
            print("Your guess is too low")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break  # Exit the loop if the guess is correct

# Call the main function
if __name__ == "__main__":
    main()
