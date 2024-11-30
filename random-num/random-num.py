import random

def main():
    # Generate and print 10 random numbers in the range 1 to 100
    for _ in range(10):
        print(random.randint(1, 100), end=" ")

# Call the main function
if __name__ == "__main__":
    main()
