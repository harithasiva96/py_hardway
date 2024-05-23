formatter = "{} {} {} {}"
  # Each pair of curly braces are replaced with corresponding arguments.
print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Hey life",
    "I am in love with you.",
    "You are opulent with your love",
    "love, and only love."
))

x = "{}"
print(x.format(1,2,3))