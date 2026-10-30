# Python Adventure Game - Search for the Legendary Treasure

def show_inventory(inventory):
    print("\nYour Inventory:")
    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        for item in inventory:
            print("-", item)


def forest_path(inventory):
    print("\nYou enter a dark forest.")
    print("You see a river and an old wooden tree.")

    print("\n1. Follow the river")
    print("2. Climb the tree")

    choice = input("Choose (1/2): ")

    if choice == "1":
        print("\nYou discover an old key near the river!")
        inventory.append("Ancient Key")
        print("Ancient Key added to inventory.")
        return True

    elif choice == "2":
        print("\nYou discover a healing potion in the tree!")
        inventory.append("Healing Potion")
        print("Healing Potion added to inventory.")
        return True

    else:
        print("Invalid choice!")
        return False


def cave_path(inventory):
    print("\nYou enter a mysterious cave.")

    print("\n1. Light a torch")
    print("2. Proceed in the dark")

    choice = input("Choose (1/2): ")

    if choice == "1":
        print("\nYou discover a hidden treasure chamber!")
        inventory.append("Treasure Map")
        print("Treasure Map added to inventory.")
        return True

    elif choice == "2":
        print("\nYou fall into a trap!")
        print("You lose the adventure.")
        return False

    else:
        print("Invalid choice!")
        return False


def treasure_chamber(inventory):
    print("\nYou have reached the final treasure chamber!")
    print("A massive locked door stands before you.")

    if "Ancient Key" in inventory:
        print("\nYou use the Ancient Key to unlock the door!")
        print("You discover the legendary treasure!")
        print("CONGRATULATIONS! YOU WIN!")
        return True

    elif "Treasure Map" in inventory:
        print("\nYour treasure map reveals a secret entrance!")
        print("You discover the legendary treasure!")
        print("CONGRATULATIONS! YOU WIN!")
        return True

    else:
        print("\nYou don't have the required item to open the door.")
        print("You have failed your quest.")
        return False


def play_game():

    while True:

        inventory = []

        print("\n================================")
        print("     THE LEGENDARY TREASURE")
        print("================================")

        name = input("\nEnter your name: ")

        print(f"\nWelcome {name}!")
        print("Your mission is to find the legendary treasure.")

        print("\nChoose your starting location:")
        print("1. Dark Forest")
        print("2. Mysterious Cave")

        choice = input("Enter choice (1/2): ")

        if choice == "1":
            result = forest_path(inventory)

        elif choice == "2":
            result = cave_path(inventory)

        else:
            print("Invalid choice!")
            continue

        if result:
            show_inventory(inventory)

            print("\nYou discover a path leading to the treasure chamber.")

            result = treasure_chamber(inventory)

        print("\nWould you like to play again?")
        print("1. Yes")
        print("2. No")

        restart = input("Enter choice: ")

        if restart != "1":
            print("\nThanks for playing!")
            break


# Start the game
play_game()