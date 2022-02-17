def digit_sum(n:int):
    number = n
    result = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        result += digit
    return result