def main():
    # Prompt the user to enter a number
    curr_value = int(input("Enter a number: "))
    
    # Double the number and print results until the value is 100 or greater
    while curr_value < 100:
        curr_value *= 2
        print(curr_value)

# Call the main function
if __name__ == "__main__":
    main()
