# P2M2 List-o-matic
# Edward Graham

def list_o_matic(location, locations):
    if location == "":
        removed = locations.pop()
        return removed + " popped from list"

    elif location in locations:
        locations.remove(location)
        return "1 instance of " + location + " removed from list"

    else:
        locations.append(location)
        return "1 instance of " + location + " appended to list"


# Starting list of Alaska locations
locations = ["Bettles", "Tanana", "Kaktovik", "Shishmaref"]

while locations:
    print("\nWelcome, Edward Graham. Look at all the Alaska locations", locations)

    location = input("Enter an Alaska location (or quit): ")

    if location.lower() == "quit":
        break

    message = list_o_matic(location, locations)
    print(message)

print("Goodbye!")