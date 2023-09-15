n = int(input("Enter the year:"))
if n % 400 == 0 and n % 100 == 0:
  print('The given year is leap year')
elif n % 4 == 0 and n % 100 != 0:
  print('The given year is leap year')
else:
  print('The given year is not a leap year')
