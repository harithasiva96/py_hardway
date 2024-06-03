i = 0
numbers = []
# Limit the value of i less than 6.
while i < 6:
    # Embed a variable i with the string.
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now:", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)