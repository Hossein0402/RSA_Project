from rsa import generate_key_pair, encrypt_text, decrypt_text


def main():
    print("Starting RSA simulation...")

    prime1 = 61
    prime2 = 53
    print(f"Chosen primes: p = {prime1}, q = {prime2}")

    print("Step 1: Generating keys...")
    public_key, private_key = generate_key_pair(prime1, prime2)
    e, n = public_key
    d, _ = private_key

    print(f"    n = {n}")
    print(f"    phi = {(prime1 - 1) * (prime2 - 1)}")
    print(f"    e = {e} (Chosen public exponent)")
    print(f"    d = {d} (Calculated private exponent)")
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    message_text = "hello im hossein"
    print("Step 2: Encrypting the message...")
    print(f"    Original Message: {message_text}")
    ciphertext_blocks, block_size = encrypt_text(public_key, message_text)
    print(f"    Encrypted Ciphertext Blocks: {ciphertext_blocks}")

    print("Step 3: Decrypting the ciphertext...")
    decrypted_message = decrypt_text(private_key, ciphertext_blocks, block_size)
    print(f"    Decrypted Message: {decrypted_message}")

    print("Verification:")
    if message_text == decrypted_message:
        print("    Original and decrypted messages match.")
        print("    RSA implementation is correct!")
    else:
        print("Error: Decryption failed.")


if __name__ == "__main__":
    main()
