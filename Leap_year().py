def is_leap_year(year):
    """
    Returns True if the given year is a leap year, otherwise False.
    Rules:
    - Years divisible by 4 are leap years,
    - Except years divisible by 100 are not leap years,
    - Except years divisible by 400 are leap years.
    """
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

# Example usage:
print("2020 →", is_leap_year(2020))
print("1900 →", is_leap_year(1900))
print("2000 →", is_leap_year(2000))
print("2021 →", is_leap_year(2021))
