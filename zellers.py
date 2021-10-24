# Zeller's algorithm computes the day of the week on which
# a specific date will fall (or fell).

print("Enter your date of birth:")
input_month = input("Month: ").upper()
if input_month.lower() == "january":
    month = 13
elif input_month.lower() == "february":
    month = 14
elif input_month.lower() == "march":
    month = 3
elif input_month.lower() == "april":
    month = 4
elif input_month.lower() == "may":
    month = 5
elif input_month.lower() == "june":
    month = 6
elif input_month.lower() == "july":
    month = 7
elif input_month.lower() == "august":
    month = 8
elif input_month.lower() == "september":
    month = 9
elif input_month.lower() == "october":
    month = 10
elif input_month.lower() == "november":
    month = 11
elif input_month.lower() == "december":
    month = 12
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

print("The day of the week that {} {}, {} falls on is {}".format(input_month, day, year, r))