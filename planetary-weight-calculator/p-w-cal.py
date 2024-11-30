# Milestone 1: Mars Weight
def calculate_mars_weight():
    earth_weight = float(input("Enter a weight on Earth: "))
    mars_weight = round(earth_weight * 0.378, 2)
    print(f"The equivalent on Mars: {mars_weight}")

# Milestone 2: Weight on All Planets
def calculate_planetary_weight():
    # Dictionary to store planet names and their gravity percentages
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    earth_weight = float(input("Enter a weight on Earth: "))
    planet_name = input("Enter a planet: ")

    # Get the gravity factor for the selected planet
    if planet_name in gravity_factors:
        gravity = gravity_factors[planet_name]
        planetary_weight = round(earth_weight * gravity, 2)
        print(f"The equivalent weight on {planet_name}: {planetary_weight}")
    else:
        print("Invalid planet name. Please try again.")

# Main Function to call the desired milestone
def main():
    print("Choose an option:")
    print("1: Calculate Mars Weight")
    print("2: Calculate Weight on Any Planet")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        calculate_mars_weight()
    elif choice == "2":
        calculate_planetary_weight()
    else:
        print("Invalid choice. Please restart the program.")

# Run the program
if __name__ == "__main__":
    main()
