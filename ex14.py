# from sys import argv

# script, user_name = argv
# prompt = '> '

# print(f"Hi {user_name}, I'm the {script} script.")
# print("I'd like to ask you a few questions.")
# print(f"Do you like me {user_name}?")
# likes = input(prompt)

# print(f"Where do you live {user_name}?")
# lives = input(prompt)

# print("What kind of computer do you have?")
# computer = input(prompt)

# print(f"""
#       Aliright, so you said {likes} about liking me.
#       You live in {lives}. Not sure where that is.
#       And you have a {computer} computer. Nice.
# """)


#Practice
from sys import argv
  # Pass all the command line argument to the script.
script, user_name = argv
  # Make an interactive enviranment.
prompt = '= '

print(f"Welcome to library {user_name}, I'm the {script} script.")
print("Welcome to the world of Bibliophiles....")
print("Would you like to take a book? ")
likes = input(prompt)

print("Which book you prefer? ")
book = input(prompt)

print("When will you return the book?")
date = input(prompt)

print(f"""
      So you said {likes} about taking a book.
      You prefer {book} book and the book will be retuened on {date}.
      Happy to see you. Have a nice date with your book."""
      )