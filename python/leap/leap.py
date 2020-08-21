
# ```text
# on every year that is evenly divisible by 4
#   except every year that is evenly divisible by 100
#     unless the year is also evenly divisible by 400
# ```

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return True if year % 400 == 0 else False
        else:
            return True
    else:
        return False
