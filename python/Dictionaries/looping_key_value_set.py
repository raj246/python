birthday_months = {
    'tony' : 'january',
    'john' : 'march',
    'steve' : 'june',
    'mike' : 'june'
}

for months in birthday_months.keys():
    print(months.title())
for month in birthday_months.values():
    print(month.title())

for birthday in set(birthday_months.values()):
    print(birthday.title())