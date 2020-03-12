def is_armstrong_number(number):
    sum_arms = 0
    for i in (str(number)):
        sum_arms += int(i)** len(str(number))

    return number == sum_arms  