print("""You enter adark room with two doors.
      Do you go through door #1 or door #2?""")
    # Prompt the user to give a reply.
door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")
    # Opt option 1 0r 2, make decision using if elif and else
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhus's retina.")
    print("1. Blueberries.")
    print("2. Yellow jackets clothespins.")
    print("3. Understanding revolves yelling melodies.")

    insanity = input("> ")
    
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
    
else:
    print("You stumble around and fall on a knife and die. Good job!")