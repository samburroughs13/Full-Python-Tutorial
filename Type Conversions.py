import datetime
birth_month = input("Birth month: ")
birth_day = int(input("Day: "))
birth_year = int(input("Year: "))

if birth_day < 10:
    birth_day = ("0" + str(birth_day))

current_month = datetime.datetime.month
current_year = datetime.datetime.year
current_day = datetime.datetime.day