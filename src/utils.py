def add(*input):
    
    sum = 0
    for element in input:
        sum += element
    
    return sum

def subtract(*input):
    
    sum = 0
    for element in input:
        sum -= element
    
    return sum

def multiply(*input):
    product = 1
    for element in input:
        product *= element

    return product


def divide(*input):
    if not input:
        return None

    quotient = input[0]
    for element in input[1:]:
        quotient /= element

    return quotient
