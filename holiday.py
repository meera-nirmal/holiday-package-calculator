# Start
# Create a function called 'hotel_cost' which: 
    # calculates and returns the total cost of a hotel based on the number of nights the user wants to stay.
# Create a function called 'plane_cost' which: 
    # returns the price of a flight depending on the city that the user wishes to visit.
# Create a function called 'car_rental' which:
    # calculates and returns the total rental cost based on the number of days the user wishes to rent the car for.
# Create a function called 'holiday_cost' which:
    # calculates the total cost based on the hotel cost, plane cost and the care rental.
# Create a dictionary called 'flight_price' which stores the names of the cities and their flight prices.
# Ask a user to enter which UK city they would like to visit out of the options and store this in a variable 
# called 'city_flight'.
    # if the user enters one of the options from 'flight_price':
        # break out of the while loop to continue onto the next code.
    # else:
        # ask the user to enter one of the options available.
# Ask the user to enter how many nights they would like to stay in a hotel for and store this in a 
# variable called 'num_nights'.
# Ask user to enter how many days they would like to hire a car for and store this in a variable called 'rental_days'.
# Print the total holiday cost.
# Print the breakdown of the cost in separate print statements for: hotel cost, plane cost and car rental.
# End

# Functions:

def hotel_cost(num_nights):
    hotel_price = num_nights * 46.72
    return hotel_price

# Uses the flight_price from the dictionary below the functions.
def plane_cost(city_flight, flight_price):
    plane_price = flight_price[city_flight]
    return plane_price
    
def car_rental(rental_days):
    total_rental_cost = rental_days * 36.50
    return total_rental_cost

# Using the variables 'cost_of_hotel', 'cost_of_plane' and 'cost_of_car_rental' 
# defined in the code below for greater readability.
def holiday_cost(hotel_cost, plane_cost, car_rental):
    total_cost = cost_of_hotel + cost_of_plane + cost_of_car_rental
    return total_cost

flight_price = {
"Belfast" : 54.60,
"Manchester" : 36.40,
"Newcastle" : 110.25,
"Southampton" : 24.80
}

while True:
    city_flight = input('''Please enter which city out of the following below you will be flying to:
Belfast
Manchester
Newcastle
Southampton
\n''').capitalize()
    
    if city_flight in flight_price:
        break

    else:
        print("\nYou have not entered one of the options available. Please try again.")

num_nights = int(input("\nPlease enter how many nights you will be staying at a hotel: "))

rental_days = int(input("\nPlease enter how many days you will be hiring a car for: "))

cost_of_hotel = hotel_cost(num_nights)

cost_of_plane = plane_cost(city_flight, flight_price)

cost_of_car_rental = car_rental(rental_days)

total_holiday_cost = holiday_cost(hotel_cost, plane_cost, car_rental)

print(f"\nThe total cost of your holiday will be £{total_holiday_cost}. Enjoy and have a safe flight!")
print("\nThe breakdown of your holiday cost is as follows: ")
print(f"The total cost for {num_nights} nights at our hotel will be £{cost_of_hotel}.")
print(f"The price of a flight to {city_flight} is £{cost_of_plane}.")
print(f"The total car rental cost for the duration of your stay will be £{cost_of_car_rental}.")