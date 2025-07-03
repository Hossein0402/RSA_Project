def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def modular_inverse(a, modulus):
    original_modulus = modulus
    x0, x1 = 0, 1
    while a > 1:
        quotient = a // modulus
        a, modulus = modulus, a % modulus
        x0, x1 = x1 - quotient * x0, x0
    return x1 + original_modulus if x1 < 0 else x1
