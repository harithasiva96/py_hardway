from sys import argv

script, input_file = argv
   # Here f refers to a file
def print_all(f):
    print(f.read())

def rewind(f):
   # Moving to the start of the file.
    print(f.seek(0))
   # line_count is a parameter that assign value from another variable 'current_line'
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now lets rewind,kind of like a tape.")
   # calling the function 'rewind'
rewind(current_file)

print("Lets print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
