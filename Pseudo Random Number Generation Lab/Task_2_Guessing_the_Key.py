import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii

# Known data
plaintext = bytes.fromhex('255044462d312e350a25d0d4c5d80a34')  # Known plaintext
ciphertext = bytes.fromhex('d06bf9d0dab8e8ef880660d2af65aa82')  # Known ciphertext
iv = bytes.fromhex('09080706050403020100A2B2C2D2E2F2')  # Known IV

# Timestamp for the file creation date (2018-04-17 23:08:49)
file_timestamp = 1523995729  # Unix timestamp for "2018-04-17 23:08:49"

# Time window: Two hours before and after
start_time = file_timestamp - 2 * 60 * 60  # 2 hours before
end_time = file_timestamp + 2 * 60 * 60    # 2 hours after

# Brute force to find the correct key
for current_time in range(start_time, end_time + 1):
    # Generate the key using current time as seed (16 bytes)
    key = current_time.to_bytes(16, byteorder='big')

    # Decrypt the ciphertext with the current key
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    except ValueError:
        # Skip invalid padding exceptions
        continue

    # Check if the decrypted data matches the expected plaintext
    if decrypted == plaintext:
        print(f"Found the key: {key.hex()}")
        break
else:
    print("No valid key found in the given time window.")
