def sum_of_multiples(limit, multiples):
    return sum(num for num in range(1, limit) if any(multiple != 0 and num % multiple == 0 for multiple in multiples))

