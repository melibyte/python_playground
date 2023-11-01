
year_1 = int(input("Enter your current year: "))
month_1 = int(input("Enter your current month: "))
day_1 = int(input("Enter your current day: "))

date_1 = (year_1 * 12 *30) + (month_1 *30) + day_1
        
year_2 = int(input("Enter the year of the old date: "))
month_2 = int(input("Enter the month of the old date: "))
day_2 = int(input("Enter the day of the old date: "))

date_2 = (year_2 * 12 * 30) + (month_2 * 30) + day_2

result = date_1 - date_2

day = int(result % 30)
month = int(result / 30) % 12
year = int(int(result / 30) /12)

second = result * 24 * 60 * 60


print(f"The difference between two dates is {year} years, {month} months, {day} days. ")

print(f"{second} seconds have passed between two dates.")
input()










