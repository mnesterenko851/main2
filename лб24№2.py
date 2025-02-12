from datetime import datetime

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def check_current_year_leap():
    current_year = datetime.now().year
    if is_leap_year(current_year):
        print(f"{current_year} рік є високосним.")
    else:
        print(f"{current_year} рік не є високосним.")

check_current_year_leap()