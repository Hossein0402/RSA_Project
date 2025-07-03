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


def text_to_blocks(text, block_size):
    byte_data = text.encode('utf-8')
    blocks = [
        int.from_bytes(byte_data[i:i + block_size], byteorder='big')
        for i in range(0, len(byte_data), block_size)
    ]
    return blocks


def blocks_to_text(blocks, block_size):
    byte_data = b''.join(
        block.to_bytes(block_size, byteorder='big') for block in blocks
    )
    return byte_data.decode('utf-8')


def encrypt_text(public_key, plaintext):
    e, n = public_key
    max_block_size = (n.bit_length() - 1) // 8
    blocks = text_to_blocks(plaintext, max_block_size)
    encrypted_blocks = [pow(block, e, n) for block in blocks]
    return encrypted_blocks, max_block_size


def decrypt_text(private_key, ciphertext_blocks, block_size):
    d, n = private_key
    decrypted_blocks = [pow(block, d, n) for block in ciphertext_blocks]
    return blocks_to_text(decrypted_blocks, block_size)
