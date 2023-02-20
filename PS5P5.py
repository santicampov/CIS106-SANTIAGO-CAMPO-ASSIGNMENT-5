#input phase
print("Please enter your last name")
name = input()
print("Please enter the number of dependents")
ndep = float(input())
print("Please enter your gross income")
gi = float(input())


#process phase
agi = gi - ndep * 12000
if agi > 50000:
    taxr = 0.2
else:
    taxr = 0.1
intax = agi * taxr
if intax <= 0:
    intax = 100


#output phase
print("For " + name)
print("With the gross income of:    $" + str(gi))
print("With " + str(ndep) + " dependents.")
print("The adjusted gross income is:    $" + str(agi))
print("The income tax is:    $" + str(intax))