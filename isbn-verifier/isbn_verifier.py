def is_valid(isbn):
    isbn = (isbn.replace('-',''))

    if len(isbn) != 10: return  False
    formula = 0

    for (i, num) in enumerate(isbn):
        if num.isnumeric():
            formula += int(num) * (10 - i)
        elif i == 9 and num is 'X':
            formula += 10
        else:
            return False

    return formula % 11 == 0



