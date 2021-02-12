def six_digit_num():
    """() -> number

    Retrun six digit number 'number' which is start with 
    100, and divisible by 9,127.

    >>> six_digit_num()
    100397
    """
    puzzle_num = []
    for num in range(100000, 101000):
        if num % 9127 == 0:
            puzzle_num.append(num)
    return puzzle_num

print(six_digit_num())