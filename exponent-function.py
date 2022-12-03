# Exponent Function

# raised to power
print(2 ** 3)


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(5, 2))


def get_pow(base_num, pow_num):
    return base_num ** pow_num


print(get_pow(3, 2))
