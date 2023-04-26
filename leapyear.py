year = int(input(" a year: "))
if (year%4==0):
    print('its a leap year')

elif (year%100==0):
    print('its a leap year')
elif(year%400==0):
    print('its a leap year')

else:
    print('its not aleap year')
