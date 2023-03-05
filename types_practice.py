firstName = input("Enter Your First Name: ")
secondName = input("Enter Your Second Name: ")

listy = [firstName, secondName]

dictionary = {
    "first": firstName,
    "last": secondName,
}
print("Print Name:", firstName, secondName)
print("List of Names:", listy)
print("Dictionary of names:", dictionary)
print("Only print last names: ", dictionary["last"])