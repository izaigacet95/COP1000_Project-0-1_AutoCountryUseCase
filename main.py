# List of authorized vehicles
AllowedVehiclesList = ["Ford F-150", "Chevrolet Silverado", "Tesla CyberTruck", "Toyota Tundra", "Nissan Titan"]

# Function to display menu
def display_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.3")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. Exit")
    print("********************************")

# Function to print all allowed vehicles
def print_authorized_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)
    print("********************************")

# Function to search for a specific vehicle
def search_vehicle():
    print("********************************")
    vehicle_name = input("Please Enter the full Vehicle name: ").strip()
    if vehicle_name in AllowedVehiclesList:
        print(f"\n{vehicle_name} is an authorized vehicle")
    else:
        print(f"\n{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again")
    print("********************************")

# Function to add a new authorized vehicle
def add_vehicle():
    print("********************************")
    new_vehicle = input("Please Enter the full Vehicle name you would like to add: ").strip()
    if new_vehicle not in AllowedVehiclesList:
        AllowedVehiclesList.append(new_vehicle)
        print(f'\nYou have added "{new_vehicle}" as an authorized vehicle')
    else:
        print(f'\n"{new_vehicle}" is already in the list of authorized vehicles')
    print("********************************")

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
        print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
        print("********************************")
        break
    else:
        print("\nInvalid choice, please try again.")
        print("********************************")
