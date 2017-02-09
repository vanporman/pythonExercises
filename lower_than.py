
def lower_than(number_1, number_2):
    if (number_1 < number_2):
        return number_1
    elif (number_2 < number_1):
        return number_2
    else:
        return "EQUAL"

lower_than(2, 1)
lower_than(10, 20)
