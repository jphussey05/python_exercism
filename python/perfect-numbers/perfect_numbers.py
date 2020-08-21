def classify(number):

    if number <= 0:
        raise ValueError('Number is unnatural')

    factors = [x for x in range(1, number // 2 + 1) if number % x == 0]

    aliquot_sum = sum(factors)

    if aliquot_sum < number:
        return 'deficient'
    elif aliquot_sum > number:
        return 'abundant'
    else:
        return 'perfect'
        