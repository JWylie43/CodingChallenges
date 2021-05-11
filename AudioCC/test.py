import math
y = []

# input the function from the user
func = input ("Enter a function f(x):\n")
print ()

for row in range (10, -11, -1):
    y_value = eval (func.replace ("x", str (row)))
    y.append (y_value)

# where the coord is defined 
for row in range (10, -11, -1):
    for column in range (-10, 11):
        # this is where the program should check for, and output a coordinate
        print ("o", end="")
        if column == 0 and row == 0:
            print ("+", end="")
        elif row == 0:
            print ("-", end="")
        elif column == 0:
            print ("|", end="")
        else:
            print (" ", end="")
    print ()