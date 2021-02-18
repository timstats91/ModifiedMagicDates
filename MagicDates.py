

# 1. Prompt user for numeric month/day/year
month = int(input('Enter a month numerically (1-12): '))
day = int(input('Enter a day of the month numerically (1-31): '))
year = int(input('Enter a four-digit year (1960): '))

# 2. Multiply month times day
magic = month * day
print('You entered a date of: ' + str(month) + '/' + str(day) + '/'\
      + str(year))

# 3. Test if month*day = year, display if magic
if magic == (abs(year) % 100):
    print('That is a magic date!')
else:
    print('That is not a magic date.')
