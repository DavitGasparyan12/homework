def check_month(age):
  if age < 0:
    print("Invalid age number. Please enter a number greater than 1.")
  elif age > 0 and age < 12:
    print("You are a child.")
  elif age > 12 and age < 17:
    print("You are a teenager.")
  elif age > 17 and age < 65:
    print("You are an adult.")
  else: age > 65
    print("You are a senior.")


age = int(input("Enter a age number (0-65 and more): "))
check_month(age)
