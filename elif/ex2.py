def check_month(month):
  if month < 1 or month > 12:
    print("Invalid month number. Please enter a number between 1 and 12.")
  elif month in (12, 1, 2):
    print("The season is Winter.")
  elif month in (3, 4, 5):
    print("The season is Spring.")
  elif month in (6, 7, 8):
    print("The season is Summer.")
  elif month in (9, 10, 11):
    print("The season is Autumn.")


month = int(input("Enter a month number (1-12): "))
check_month(month)
