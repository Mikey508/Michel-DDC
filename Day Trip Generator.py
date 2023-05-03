import random

destinations = ['Boston', 'New York', 'London']
restaurants = ['Ihop', 'Moes', 'Panda Express', 'Texas Raod House']
transportation = ['Stubborn Horse', 'Pogo Stick', 'Little Tikes', 'unicycle' 'office chair']
entertainment = ['A Lounge', 'Comedy Show', 'Live Sports', 'Gaming']

destination = random.choice(destinations)
restaurant = random.choice(restaurants)
transport = random.choice(transportation)
activity = random.choice(entertainment)

print("Your day trip plan:")
print("Destination: " + destination)
print("Restaurant: " + restaurant)
print("Transportation: " + transport)
print("Entertainment: " + activity)

