from math_lib import is_prime, gcd, modular_inverse


def generate_key_pair(prime1, prime2):
    if not (is_prime(prime1) and is_prime(prime2)):
        raise ValueError("Both numbers must be prime.")
    if prime1 == prime2:
        raise ValueError("Primes must be distinct.")

    modulus = prime1 * prime2
    totient = (prime1 - 1) * (prime2 - 1)

    public_exponent = 65537
    if gcd(public_exponent, totient) != 1:
        public_exponent = 3
        while gcd(public_exponent, totient) != 1:
            public_exponent += 2

    private_exponent = modular_inverse(public_exponent, totient)

    public_key = (public_exponent, modulus)
    private_key = (private_exponent, modulus)

    return public_key, private_key
