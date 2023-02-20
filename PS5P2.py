#input phase
print("Please enter the item code. (A or B).")
item = input()
print("Now, please enter the item quantity.")
qty = float(input())


#process phase
if item == "A":
    up = 10.0
else:
    up = 20.0
ep = qty * up


#output phase
print("For " + str(qty) + " units of item " + item)
print("The Unit price is:     $" + str(up))
print("The extended price is:     $" + str(ep))