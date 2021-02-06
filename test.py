#This is function to count max number
def max_number(list):
    number = 0
    for item in list:
        if item > number:
            number = item
    return number

print(max_number([3,6,8,1,0,4,6,16,4,8]))
