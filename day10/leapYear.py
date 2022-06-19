def leap(year):
    # below is an example od docstring
    """ This takes in account the entered year and checks whether it is leap or non-leap year"""
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    if month>12 or month<1:
        return "Invalid month"
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leap(year) and month ==2:
        return 29
    else:
        return days[month-1]


year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
days = days_in_month(year,month)
print(days)