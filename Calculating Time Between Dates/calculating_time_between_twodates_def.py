
def date_1():
    year_1 = int(input("Enter your current year: "))
    month_1 = int(input("Enter your current month: "))
    day_1 = int(input("Enter your current day: "))

    return (year_1 * 12 *30) + (month_1 *30) + day_1

def date_2():
    year_2 = int(input("Enter the year of the old date: "))
    month_2 = int(input("Enter the month of the old date: "))
    day_2 = int(input("Enter the day of the old date: "))

    return (year_2 * 12 * 30) + (month_2 * 30) + day_2

def result():
    return a - b

a = date_1()
b = date_2()
c = result()

def second():
    return c * 24 * 60 * 60

def day():
    day = int(c % 30)
    return day

def month():
    month = int(c / 30) % 12
    return month


def year():
    year = int(int(c / 30) /12)
    return year




print(f"The difference between two dates is {year()} years, {month()} months, {day()} days. ")

print(f"{second()} seconds have passed between two dates.")
input()


