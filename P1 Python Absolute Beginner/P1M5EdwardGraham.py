def adding_report(report="T"):
    total = 0
    items = ""

    print('Input an integer to add to the total or "Q" to quit')

    while True:
        number = input('Enter an integer or "Q": ')

        if number.isdigit():
            total = total + int(number)

            if report == "A":
                items = items + number + "\n"

        elif number.upper().startswith("Q"):
            if report == "A":
                print("\nItems")
                print(items)
                print("Total")
                print(total)
            else:
                print("\nTotal")
                print(total)

            print("Calculated by: Edward Graham")
            break

        else:
            print(number, "is invalid input")


adding_report("A")
adding_report("T")

