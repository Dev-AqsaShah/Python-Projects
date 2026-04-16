from datetime import date

birthdate = date(2002, 9, 17)

today = date.today()

difference = today - birthdate

days_old = difference.days

print(f"your birthdate: {birthdate}")
print(f"today's date: {today}")
print(f"you are {days_old} days old!")
