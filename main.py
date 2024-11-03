# List of authorized vehicles
AllowedVehiclesList = ["Ford F-150", "Chevrolet Silverado", "Tesla CyberTruck", "Toyota Tundra", "Nissan Titan"]

# Function to display menu
def display_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")

# Function to print all allowed vehicles
def print_authorized_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)
   

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        print_authorized_vehicles()
    elif choice == "2":
        print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
        break
    else:
        print("\nInvalid choice, please try again.")
