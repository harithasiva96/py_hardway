from sys import exit

def magic_palace():
    print("There is room full of gold. Lets steal?")

    choice = input("> ")
    if choice == "yes":
        print("Such a greedy. You loose the chance.")
        # exit the process.
        exit(0)
    elif choice == "no":
        # Take to the function plants.
        plants()
    else:
        print("You are confused. End game")
        exit(0)
        
def plants():
    print("Would you like to pluck the flowers or water the plants?")

    choice = input("> ")
    if choice == "pluck":
        print("OOh No man you lose the game.")
    elif choice == "water":
        print("You are so sweet. Take the gold. You winnnnnnn!!")

def mistry_forest():
    print("Great!!! Let's explore the forest!")
    print("What you prefer hunt or plant?")
    choice = input("> ")

    if choice == "hunt":
        print("You are so cruel. Let the tiger eat you. You loose.")
    elif choice == "plant":
        print("You are so sweet. Take the gold. You winnnnnnn.")

def start():
    print("Weicome to Treasure hunt!!!!")
    print("What would you like to choose? palace or forest?")

    choice = input("> ")

    if choice == "palace":
        magic_palace()
    elif choice == "forest":
        mistry_forest()
    else:
        print("You dont dare to choose. Such a coward. You are dead.")

start()
