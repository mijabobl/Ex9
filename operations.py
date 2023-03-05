var = input("Please enter a value: ")

print("Upper Case: ", var.upper())
print("No. of characters is: ", len(var))

dec = any(var.isdecimal() for var in var)

if dec == False:
        print("There are no numeric characters here")
else:
        print("There are numeric characters here")