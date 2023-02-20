#input process
print("Please enter the quantity.")
qty = float(input())

#process phase
if qty >= 1000:
  up = 3.00
else:
  up = 5.00
extpc = qty * up
tax = extpc * 0.07
total = extpc + tax

#output phase
print("Quantity of units ordered:   ", qty)
print("Unit Price:  $", up)
print("Extended price:   $", extpc)
print("Tax:    $", tax)
print("Total order:  $", total)