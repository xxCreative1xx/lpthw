#This is the number of cars available
cars = 100
#This shows how many seats are in each car
space_in_a_car = 4
#Number of available drivers
drivers = 30
#Number of passengers needing transportation
passengers = 90
#Number of cars which cannot be driven
cars_not_driven = cars - drivers
#How many cars will be driven
cars_driven = drivers
#Total number of seats available
carpool_capacity = cars_driven * space_in_a_car
#Average number of passengers per car
average_passengers_per_car = passengers / cars_driven


print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")