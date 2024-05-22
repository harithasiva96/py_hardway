  # Here the variables are assigned a value
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
  # Cars and drivers are variables that already assigned values. 
  # The difference of their values are assigned to another variable.
cars_not_driven = cars - drivers
cars_driven = drivers
car_pool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

  # Car is a variable with value 100. While printing, value is taken for execution.
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There are only", drivers, "drivers available.")
print("We can transport", car_pool_capacity , "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")