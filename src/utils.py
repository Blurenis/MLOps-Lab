def add(*values):
    total = 0
    for element in values:
        total += element
    print("ioferfoierhjhfioerhjfoierjfoijr")
    print("pfjeifjerjfoerijfoerijferoijfoerij")

    return total


def subtract(*values):
    if not values:
        return 0
    result = values[0]
    for element in values[1:]:
        result -= element
    return result


def multiply(*values):
    product = 1
    for element in values:
        if not isinstance(element, (int, float)):
            raise TypeError("multiply() accepte seulement int ou float")
        product *= element
    return product


def divide(*values):
    if not values:
        return None
    quotient = values[0]
    for element in values[1:]:
        quotient /= element
    return quotient
