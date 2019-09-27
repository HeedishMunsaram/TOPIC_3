name_1 = input("Please enter a name: ")
length = len(name_1) -1
indnum = int(input("Please enter a character number 0-" + str(length) + ": "))

if indnum >= length:
    print("Error! Invalid Input")
else:
    print(name_1)