def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!.")
    print("Get a blanket.\n")

# Different ways to pass arguments through parameters.
 # Assign the values directly.
cheese_and_crackers(20,30)

 # Use variables.
cheese = 50
crackers = 70 
cheese_and_crackers(cheese, crackers)

  # Usage of math and variables
cheese_and_crackers(20+30, 40+20)
cheese_and_crackers(cheese+40, crackers+20)