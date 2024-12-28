import time
import random

# Case 1: Using a seed for the random number generator
print("-----------------------------")
print("Case 1: Using a seed (time-based):")
print("-----------------------------")

KEYSIZE = 16



def generate_key_from_timestamp(timestamp):
    # Use the timestamp as the seed for random number generation
    random.seed(timestamp)

    # Generate a 16-byte encryption key
    key = [random.randint(0, 255) for _ in range(KEYSIZE)]

    # Convert the key to hexadecimal format and print it
    hex_key = ''.join([format(byte, '02x') for byte in key])

    return hex_key


# Define a specific timestamp (e.g., "2018-04-17 23:08:49")
timestamp = 1523995729  # This is the Unix timestamp for "2018-04-17 23:08:49"

# Generate the key from the timestamp
key = generate_key_from_timestamp(timestamp)

# Print the generated encryption key
print(key)
print("\n")

# Case 2: Without using a seed for the random number generator
print("-----------------------------")
print("Case 2: Without using a seed:")
print("-----------------------------")
random.seed(None)  # This sets the seed to a default state
key = bytearray()
for i in range(KEYSIZE):
    key.append(random.randint(0, 255))  # Generate a random byte
    print(f"{key[i]:02x}", end="")  # Print each byte as a two-digit hex value
print("\n")
