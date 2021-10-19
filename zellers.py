# Zeller's algorithm computes the day of the week on which
# a specific date will fall (or fell).

print("Enter your date of birth:")
month = input("Month: ")
if month.lower() == "january":
    month = 11
elif month.lower() == "february":
    month = 12
elif month.lower() == "march":
    month = 1
elif month.lower() == "april":
    month = 2
elif month.lower() == "may":
    month = 3
elif month.lower() == "june":
    month = 4
elif month.lower() == "july":
    month = 5
elif month.lower() == "august":
    month = 6
elif month.lower() == "september":
    month = 7
elif month.lower() == "october":
    month = 8
elif month.lower() == "november":
    month = 9
elif month.lower() == "december":
    month = 10
day = int(input("Day: "))
year = input("Year: ")
year_of_century = int(year[2:4])
century = int(year[0:2])

w = (13 * month - 1) / 5
x = year_of_century / 4
y = century / 4
z = w + x + y + day + year_of_century - 2*century
r = round(z % 7,0)
if r == 0:
    r = "Sunday"
elif r == 1:
    r = "Monday"
elif r == 2:
    r = "Tuesday"
elif r == 3:
    r = "Wednesday"
elif r == 4:
    r = "Thursday"
elif r == 5:
    r = "Friday"
elif r == 6:
    r = "Saturday"

print(r)