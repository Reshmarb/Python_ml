year = int(input(" a year: "))
if (year%4==0 and year%100==0 and year%400==0):
    print('its a leap year')

else:
    print('its not a leap year')
