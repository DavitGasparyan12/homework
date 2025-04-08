number = int(input("Enter a number: "))
# if number is divide to 7 and not dividing to 3 print (the number is true)
if number % 7 == 0 and number % 3 != 0:
    print(f"this number-{number} is True")
else:
    print(f"this number-{number} is False")
