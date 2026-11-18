# P2M5 Final Project - Element Quiz
# Edward Graham

import os
import urllib.request

def get_names():
    names = []

    while len(names) < 5:
        element = input("Enter the name of an element: ").strip().lower()

        if element == "":
            print("Please enter an element name.")
        elif element in names:
            print(element + " was already entered")
        else:
            names.append(element)

    return names


def Element_Quiz():
    print("Welcome Edward Graham, list any 5 of the first 20 elements in the Periodic table")

    file_name = "elements1_20.txt"
    file_url = "https://raw.githubusercontent.com/MicrosoftLearning/introPython/master/elements1_20.txt"

    if not os.path.isfile(file_name):
        urllib.request.urlretrieve(file_url, file_name)

    elements = []

    element_file = open(file_name, "r")

    for i in range(20):
        element = element_file.readline().strip().lower()

        if element != "":
            elements.append(element)

    element_file.close()

    responses = get_names()

    correct = []
    incorrect = []

    for response in responses:
        if response in elements:
            correct.append(response)
        else:
            incorrect.append(response)

    score = (len(correct) / 5) * 100

    print()
    print(str(int(score)) + " % correct")

    print("Found:", end=" ")
    for element in correct:
        print(element.title(), end=" ")

    print()

    print("Not Found:", end=" ")
    for element in incorrect:
        print(element.title(), end=" ")

    print()


Element_Quiz()