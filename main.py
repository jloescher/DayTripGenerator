import random

# (5 points): As a developer, I want to make at least three commits with descriptive messages 

# (5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists.
destinations = ["New York", "Tampa", "Miami", "Chicago", "Atlanta", "San Francisco"]
restaurants = [["Kochi", "Crown Shy", "Dhamaka", "Gage & Tollner"], ["Vino E Pasta", "Happy Fish", "Wright's Gourmet House", "Terra Gaucha Brazilian Steakhouse Tampa"], ["Stubborn Seed", "Boia De", "La Mar", "The Surf Club Restaurant"], ["Superdawg Drive-In", "Luella's Southern Kitchen", "Bayan Ko", "Community Tavern"], ["Spring Restaurant", "Minas Grill & Emporium", "Virgil's Gullah Kitchen & Bar", "Heirloom Market BBQ"], ["Abacá", "Lucca Delicatessen", "Sotto Mare", "Restaurant Nisei"]]
transportation = ["train", "bus", "plane", "boat"]
entertainment = ["concert", "theatre", "sight seeing", "cultural sites", "historic sites"]

# (5 points): As a user, I want a destination to be randomly selected for my day trip.
session_destination = ""

def random_destination():
  random = random.randint(0, len(destinations))
  return destinations[random]

def destination_sequence():
  session_destination = random_destination()
  print(f"Your random destination is {session_destination}")
  destination_confirm = input(f"Are you happy with {session_destination} as your destination or would you like to choose another destination? Y or N")
  return destination_confirm.lower()

running = True
while running:
  destination_confirm = destination_sequence()
  match destination_confirm:
    case "y":
      destination_confirm = destination_sequence()
    case "n":
      session_destination = session_destination
      break

# (5 points): As a user, I want a restaurant to be randomly selected for my day trip

# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 

# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

# (10  points): As a user, I want to display my completed trip in the console

# (5 points): Single Responsibility: As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing! 
