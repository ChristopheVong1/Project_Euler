from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def smallest_multiple(max_num):
    result = 1
    for i in range(1, max_num + 1):
        result = lcm(result, i)
    return result

print(smallest_multiple(20))  # Output: 232792560