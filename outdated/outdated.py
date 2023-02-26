# Problem Set: https://cs50.harvard.edu/python/2022/psets/3/outdated/

""" 
implement a program that prompts the user for a date, anno Domini, 
in month-day-year order, formatted like 9/8/1636 or September 8, 1636, 
wherein the month in the latter might be any of the values in the list below:
Then output that same date in YYYY-MM-DD format. 
If the user’s input is not a valid date in either format, prompt the user again. 
Assume that every month has no more than 31 days; 
no need to validate whether a month has 28, 29, 30, or 31 days.
 """

months = [
    "January", # 0 + 1
    "February", # 1
    "March", # 2
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Nested Try-Except
while True:
    try: # lets you test a block of code for errors
        # user prompt
        date_input = input("Date: ").title()
        # September 8, 2022
        month_date, year = date_input.split(",") # September 8, 2022
        month, date = month_date.split()
            # month = September, date = 8, year = 2022
            # assigning number to the month
        if month in months:
            month_num = months.index(month) + 1 # int
        else:
            continue
        date, year = int(date), int(year) # convert date year into int
        if (month_num >= 1 and month_num <= 12) and (date >= 1 and date <= 31):
            print(f"{year:04}-{month_num:02}-{date:02}")
            break
        else:
            continue
    except Exception as e:
        print(e) 
        try:
            month_2, date_2, year_2 = date_input.split("/")
            month_2, date_2, year_2 = int(month_2), int(date_2), int(year_2)
            if (month_2 >= 1 and month_2 <= 12) and (date_2 >= 1 and date_2 <= 31):
                print(f"{year_2:04}-{month_2:02}-{date_2:02}")
                break
        except (ValueError):
            pass