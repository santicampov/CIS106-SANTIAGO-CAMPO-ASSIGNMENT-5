#input phase
print("Please enter the amount of books you want to order.")
qty = float(input())
print("Please enter the Cost per book.")
cpb = float(input())


#process phase
subtotal = qty * cpb
if subtotal > 50.0:
    ship = 0
else:
    ship = 25
total = subtotal + ship


#output phase
print("The subtotal is:     $" + str(subtotal))
print("Shipping fee of:     $" + str(ship))
print("The order total is:     $" + str(total))