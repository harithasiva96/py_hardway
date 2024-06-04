# Assigning variable a value.
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")
# Spliting the string assigned to the variable 'ten_things'.
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
# 
while len(stuff) != 10:
    # Poping the elements one by one from "more_stuff" to make 10 elements in 'stuff'.
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    # Append the popped element to the splitted string 'stuff'
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")
# Get the second element which has the index number 1.
print(stuff[1])
# Print the last element.
print(stuff[-1]) #whoa! fancy
# Simply pop() attribute gives the last element.
print(stuff.pop())
print(''.join(stuff)) # what? cool!
print('#'.join(stuff[3:5])) # super stellar!