import random

# (5 points): As a developer, I want to make at least three commits with descriptive messages

# (5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists.
destinations = ["New York", "Tampa", "Miami", "Chicago", "Atlanta", "San Francisco"]
restaurants = [
    ["Kochi", "Crown Shy", "Dhamaka", "Gage & Tollner"],
    [
        "Vino E Pasta",
        "Happy Fish",
        "Wright's Gourmet House",
        "Terra Gaucha Brazilian Steakhouse Tampa",
    ],
    ["Stubborn Seed", "Boia De", "La Mar", "The Surf Club Restaurant"],
    ["Superdawg Drive-In", "Luella's Southern Kitchen", "Bayan Ko", "Community Tavern"],
    [
        "Spring Restaurant",
        "Minas Grill & Emporium",
        "Virgil's Gullah Kitchen & Bar",
        "Heirloom Market BBQ",
    ],
    ["Abacá", "Lucca Delicatessen", "Sotto Mare", "Restaurant Nisei"],
]
transportation_list = ["train", "bus", "plane", "boat"]
entertainment_list = [
    "concert",
    "theatre",
    "sight seeing",
    "cultural sites",
    "historic sites",
]

destination_index = 0
selected_destination = ""
destination_run = 0

selected_restaurant = ""

selected_transportation = ""

selected_entertainment = ""


# (5 points): As a user, I want a destination to be randomly selected for my day trip.
def destination():
    destination_response = dict()
    while True:
        # Generate a random number between 0 and the length of the destinations list
        destination_index = random.randint(0, len(destinations) - 1)

        # Use the random number to select a destination
        selected_destination = destinations[destination_index]
        print(f"Your randomly selected destination is: {selected_destination}")

        # Prompt the user to accept the selected destination
        response = input("Do you want to go to this destination (y/n)? ")

        destination_response["destination_index"] = destination_index
        destination_response["selected_destination"] = selected_destination

        # If the user accepts the destination, exit the loop
        if response.lower() == "y":
            break

    count = destination_run + 1
    destination_response["destination_run"] = count
    return destination_response


# (5 points): As a user, I want a restaurant to be randomly selected for my day trip
def restaurant():
    while True:
        # Generate a random number between 0 and the length of the restaurants list
        restaurant_index = random.randint(0, len(restaurants[destination_index]) - 1)

        # Use the random number to select a restaurant
        selected_restaurant = restaurants[destination_index][restaurant_index]
        print(f"Your randomly selected restaurant is: {selected_restaurant}")

        # Prompt the user to accept the selected restaurant
        response = input("Do you want to go to this restaurant (y/n)? ")

        # If the user accepts the restaurant, exit the loop
        if response.lower() == "y":
            break

    return selected_restaurant


# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.
def transportation():
    while True:
        # Generate a random number between 0 and the length of the transportation list
        transportation_index = random.randint(0, len(transportation_list) - 1)

        # Use the random number to select a mode of transportation
        selected_transportation = transportation_list[transportation_index]
        print(
            f"Your randomly selected mode of transportation is: {selected_transportation}"
        )

        # Prompt the user to accept the selected mode of transportation
        response = input("Do you want to use this mode of transportation (y/n)? ")

        # If the user accepts the mode of transportation, exit the loop
        if response.lower() == "y":
            break

    return selected_transportation


# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
def entertainment():
    while True:
        # Generate a random number between 0 and the length of the entertainment list
        entertainment_index = random.randint(0, len(entertainment_list) - 1)

        # Use the random number to select a form of entertainment
        selected_entertainment = entertainment_list[entertainment_index]
        print(
            f"Your randomly selected form of entertainment is: {selected_entertainment}"
        )

        # Prompt the user to accept the selected mode of entertainment
        response = input("Do you want to use this mode of entertainment (y/n)? ")

        # If the user accepts the mode of entertainment, exit the loop
        if response.lower() == "y":
            break

    return selected_entertainment


destination_response = destination()
destination_index = destination_response["destination_index"]
selected_destination = destination_response["selected_destination"]
destination_run = destination_response["destination_run"]
restaurant_response = restaurant()
selected_restaurant = restaurant_response
transportation_response = transportation()
selected_transportation = transportation_response
entertainment_response = entertainment()
selected_entertainment = entertainment_response

# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

while True:
    print("You have selected the following items for your daytrip:")
    print(f"Destination: {selected_destination}")
    print(f"Restaurant: {selected_restaurant}")
    print(f"Transportation: {selected_transportation}")
    print(f"Entertainment: {selected_entertainment}")
    print(
        "Please confirm if this is acceptable, if not please identify the category you would like to change: "
    )
    print("1. Destination")
    print("2. Restaurant")
    print("3. Transportation")
    print("4. Entertainment")
    print("5. All is good, let's hit the road!")
    user_confirm_update = input(
        "Please enter the respective number of your selection: "
    )
    match int(user_confirm_update):
        case 1:
            destination_response = destination()
            destination_index = destination_response["destination_index"]
            selected_destination = destination_response["selected_destination"]
            destination_run = destination_response["destination_run"]
            if destination_run > 1:
                restaurant_response = restaurant()
                selected_restaurant = restaurant_response
        case 2:
            restaurant_response = restaurant()
            selected_restaurant = restaurant_response
        case 3:
            transportation_response = transportation()
            selected_transportation = transportation_response
        case 4:
            entertainment_response = entertainment()
            selected_entertainment = entertainment_response
        # (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
        case 5:
            # (10  points): As a user, I want to display my completed trip in the console
            print(
                f"Your trip to {selected_destination} by {selected_transportation} where you will eat at {selected_restaurant} and enjoy a {selected_entertainment} is scheduled."
            )
            break


# (5 points): Single Responsibility: As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!
