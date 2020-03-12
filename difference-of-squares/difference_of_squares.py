def square_of_sum(number):
    squ_sum = 0
    for i in range(1, number+1):
        squ_sum += i
    squ_sum = squ_sum**2    
    return squ_sum 


def sum_of_squares(number):
    sum_squ = 0
    for i in range(1, number+1):
        sum_squ += i**2
    return sum_squ 


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)