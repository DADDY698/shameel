def manager_menu(name):
    while True:
        print("\n~~~~~~ Manager Menu ~~~~~~")
        print("1. Manage Customers")
        print("2. Manage Menu Categories and Pricing")
        print("3. View Ingredients List Requested by Chef")
        print("4. Update Profile")
        print("5. Logout")
        selection = input("Select an option: ")

        match selection:
            case "1":
                manage_customers()
            case "2":
                manage_menu()
            case "3":
                view_ingredients_list()
            case "4":
                update_profile(name)
            case "5":
                print("Thank you. Have a good day!")
                break
            case _:
                print("Invalid input. Please try again!")
# --- manager menu ends ---

# --- manage customers function starts ---
def manage_customers():
    while True:
        print("\n~~~~~~ Manage Customers ~~~~~~")
        print("1. Add Customer")
        print("2. Edit Customer")
        print("3. Delete Customer")
        print("4. Back to Manager Menu")
        selection = input("Select an option: ")

        match selection:
            case "1":
                add_customer()
            case "2":
                edit_customer()
            case "3":
                delete_customer()
            case "4":
                break
            case _:
                print("Invalid input. Please try again!")

# Add customer function
def add_customer():
    print("Enter the details to add customer: ")
    id = input("Enter customer ID: ")
    name = input("Enter customer name: ")
    username = input("Enter username: ")
    email = input("Enter email address: ")
    password = username + "123"
    role = "customer"
    with open("user.txt", "a") as file:
        file.write(f"{id}.{name},{username},{email},{password},{role}\n")
    print("Customer added successfully!")

# Edit customer function
def edit_customer():
    username = input("Enter the username of the customer: ")
    data = []
    found = False

    with open("user.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if info[1] == username and info[4] == "customer":
                found = True
                print("\nWhat would you like to edit?")
                print("1. Name")
                print("2. Username")
                print("3. Email")
                print("4. Password")
                print("5. Back")

                selection = int(input("Choose the option you want to edit: "))

                match selection:
                    case 1:
                        info[0] = input("\nEnter the new name: ")
                    case 2:
                        info[1] = input("\nEnter the new username: ")
                    case 3:
                        info[2] = input("\nEnter the new email: ")
                    case 4:
                        info[3] = input("\nEnter the new password: ")
                    case 5:
                        print("Back to menu\n")
                        return
                    case _:
                        print("Invalid selection! Please choose a valid option.")

            data.append(info)

    with open("user.txt", "w") as file:
        for line in data:
            file.write(f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]}\n")

    if found:
        print("Customer edited successfully!")
    else:
        print("No matching customer found.")

# Delete customer function
def delete_customer():
    username = input("Enter the username of the customer to delete: ")
    data = []
    found = False

    with open("user.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if info[1] == username and info[4] == "customer":
                found = True
            else:
                data.append(info)

    with open("user.txt", "w") as file:
        for line in data:
            file.write(f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]}\n")

    if found:
        print("Customer deleted successfully!")
    else:
        print("No matching customer found.")

# --- manage customers function ends ---

# --- manage menu function starts ---