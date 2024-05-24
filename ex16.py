from sys import argv

script, filename = argv

print("We are going to erase f{filename}.")
print("If you dont want that, hit CTRL-C (^C).")
print(("If you do want that, hit return."))

input("?")

print("Opening the file...")
  # Open the file and switch on write mode.
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
  # Truncate empties the file.
target.truncate()

print("Now I am going to ask you for three lines.")
  # The required lines to be added.
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I am going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print("And finallly, we close it.")
target.close()