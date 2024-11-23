# File containing the authorized vehicles
filename = "allowed_vehicles.txt"


# Function to initialize the file with the default list
def initialize_file():
    try:
        with open(filename, 'r') as file:
            # If the file exists, do nothing
            pass
    except FileNotFoundError:
        # If the file doesn't exist, create it with the default vehicles
        default_vehicles = [
            "Ford F-150", "Chevrolet Silverado", "Tesla CyberTruck",
            "Toyota Tundra", "Rivian R1T", "Ram 1500"
        ]
        with open(filename, 'w') as file:
            for vehicle in default_vehicles:
                file.write(vehicle + "\n")


# Function to read all vehicles from the file
def read_vehicles():
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]


# Function to write the list of vehicles back to the file
def write_vehicles(vehicles):
    with open(filename, 'w') as file:
        for vehicle in vehicles:
            file.write(vehicle + "\n")


# Function to display menu
def display_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.4")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("********************************")


# Function to print all allowed vehicles
def print_authorized_vehicles():
    vehicles = read_vehicles()
    print(
        "\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:"
    )
    for vehicle in vehicles:
        print(vehicle)
    print("********************************")


# Function to search for a specific vehicle
def search_vehicle():
    print("********************************")
    vehicle_name = input("Please Enter the full Vehicle name: ").strip()
    vehicles = read_vehicles()
    if vehicle_name in vehicles:
        print(f"\n{vehicle_name} is an authorized vehicle")
    else:
        print(
            f"\n{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again"
        )
    print("********************************")


# Function to add a new authorized vehicle
def add_vehicle():
    print("********************************")
    new_vehicle = input(
        "Please Enter the full Vehicle name you would like to add: ").strip()
    vehicles = read_vehicles()
    if new_vehicle not in vehicles:
        vehicles.append(new_vehicle)
        write_vehicles(vehicles)
        print(f'\nYou have added "{new_vehicle}" as an authorized vehicle')
    else:
        print(
            f'\n"{new_vehicle}" is already in the list of authorized vehicles')
    print("********************************")


# Function to delete a vehicle from the file
def delete_vehicle():
    print("********************************")
    vehicle_name = input(
        "Please Enter the full Vehicle name you would like to REMOVE: ").strip(
        )
    vehicles = read_vehicles()
    if vehicle_name in vehicles:
        confirmation = input(
            f'Are you sure you want to remove "{vehicle_name}" from the Authorized Vehicles List? (yes/no): '
        ).strip().lower()
        if confirmation == "yes":
            vehicles.remove(vehicle_name)
            write_vehicles(vehicles)
            print(
                f'You have REMOVED "{vehicle_name}" as an authorized vehicle')
        else:
            print("Vehicle removal canceled.")
    else:
        print(
            f'"{vehicle_name}" is not found in the list of authorized vehicles'
        )
    print("********************************")


# Initialize the file with default values if it doesn't exist
initialize_file()

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        print_authorized_vehicles()
    elif choice == "2":
        search_vehicle()
    elif choice == "3":
        add_vehicle()
    elif choice == "4":
        delete_vehicle()
    elif choice == "5":
        print(
            "\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
        print("********************************")
        break
    else:
        print("\nInvalid choice, please try again.")
        print("********************************")
