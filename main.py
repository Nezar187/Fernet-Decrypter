from cryptography.fernet import Fernet
import os
os.system("pip install Fernet")
def decrypt_message(encrypted_message, key):
    # Instantiate a Fernet object with the provided key
    cipher_suite = Fernet(key)

    # Decrypt the message
    decrypted_message = cipher_suite.decrypt(encrypted_message)

    return decrypted_message.decode('utf-8')

# Example usage:
key = b'key'  # Make sure to use a byte string
encrypted_message = b'message'

# Decrypt the message
decrypted_message = decrypt_message(encrypted_message, key)

print(f"Decrypted message: {decrypted_message}")
with(open("decrypted_message.txt", "w")) as f:
  f.write(decrypted_message)
