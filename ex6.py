  # Assigning variable a value
types_of_people = 10
  # Format string f is used with in a string to add a variable.
x = f"There are {types_of_people} types of people."
  # Assigning variable a string
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)
  # Formating an already formated string.
print(f"I said: {x}")
print(f"I also said: {y}")


hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
  # Applying variable hilarious in a format- .format() syntax
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
  # Adding two strings
print(w + e)
