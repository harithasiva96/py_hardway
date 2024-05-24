# from sys import argv

# script, filename = argv

# txt = open(filename)

# print("Here is your file {filename}:")
# print(txt.read())

# print("Type the file name again:")
# file_again = input("> ")

# txt_again = open(file_again)

# print(txt_again.read())

   # Practice- Read a python script.
   # Not only text file, we can open any file.
from sys import argv

script, filename = argv

txt = open(filename)
    
print("Here is your file {Filename}:")
print(txt.read())
   # Type the nam eof the file to be read.
print("Type the file name again:")
file_again = input("> ")

txt_again = open(file_again)
  # Print the txt that has already read.
print(txt_again.read())