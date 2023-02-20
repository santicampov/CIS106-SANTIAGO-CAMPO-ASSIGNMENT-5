#input phase
print("Please enter the name of the appliance.")
name = input()
print("Please enter the cost of the appliance.")
cost = float(input())


#process phase
if cost > 1000:
    wrty = cost * 0.1
else:
    wrty = cost * 0.05
total = cost + wrty


#output phase
print("For the appliance " + name + " with the cost of: $" + str(cost))
print("The cost of the warranty is: $" + str(wrty))
print("Total price of:  $" + str(total))