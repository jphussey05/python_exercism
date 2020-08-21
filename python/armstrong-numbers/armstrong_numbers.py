def is_armstrong_number(number):
    nums = list(map(int,(str(number))))
    num_digits = len(nums)
    total = 0
    for num in nums:
        total += (num**num_digits)

    return True if total == number else False
