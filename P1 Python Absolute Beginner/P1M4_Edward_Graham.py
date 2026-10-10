
# Graham P1M4 .py assignment 
# [ ] create, call and test the str_analysis() function  



def str_analysis(user_text):
    if user_text.isdigit():
        number = int(user_text)
        if number > 99:
            return user_text + " is a large number!"
        else:
            return user_text + " is a relatively small number."
    else:
        if user_text.isalpha():
            return '"' + user_text + '" contains only letters.'
        else:
            return '"' + user_text + '" contains a mixture of characters.'


# Call input and make sure something is entered
user_input = ""

while user_input == "":
    user_input = input("Edward Graham - Enter a word or number: ")

# Check input and display result

print(str_analysis(user_input))
