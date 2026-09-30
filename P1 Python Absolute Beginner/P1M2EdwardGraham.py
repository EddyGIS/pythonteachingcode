# [ ] create, call and test fishstore() function 
def fishstore(fish, price):
    return "Fish Type: " + fish.title() + " costs $" + price

fish_entry = input("Enter fish type: ")
price_entry = input("Enter fish price: ")

fish_report = fishstore(fish_entry, price_entry)

print("Report for Edward Graham.", fish_report)

