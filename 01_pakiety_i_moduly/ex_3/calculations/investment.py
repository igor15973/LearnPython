import math
def investment_value(starting_capital, percentage, years):
    value = starting_capital * math.pow((1 + percentage / 100),years)
    return value

