num_1 = int(input("Enter a number 1: "))
num_2 = int(input("Enter a number 2: "))
num_3 = int(input("Enter a number 3: "))

if num_1 > num_2:
    print("A is greater")
elif num_2 > num_3:
    print("B is greater")
elif num_3 > num_1:
    print("C is greater")
else:
    print("Invalid number")