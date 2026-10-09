# [ ] create function, call and test

def cheese_order(order_amount, max=76, min=1, price=5.49):
    order_amount = float(order_amount)
    max = float(max)
    min = float(min)
    price = float(price)

    if order_amount > max:
        print(str(order_amount) + " is more than currently available stock")
    elif order_amount < min:
        print(str(order_amount) + " is below minimum order amount")
    else:
        cost = round(order_amount * price, 2)
        print(str(order_amount) + " costs $" + str(cost))

weight = input("Edward Graham, enter cheese order weight (numeric value): ")
cheese_order(weight)