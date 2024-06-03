def leap(year):
    return f"{year} is leap year" if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else f"{year} is not a leap year" 

year = int(input())
print(leap(year))