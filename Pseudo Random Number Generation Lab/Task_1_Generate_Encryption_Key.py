import time
import random

KEYSIZE = 16  # Define the key size (16 bytes = 128 bits)

# Case 1: Using a seed for the random number generator
print("Case 1: Using a seed (time-based):")
seed = int(time.time())  # Get the current time in seconds since the Epoch
print(f"Seed: {seed}")
random.seed(seed)  # Seed the random number generator
key = bytearray()
for i in range(KEYSIZE):
    key.append(random.randint(0, 255))  # Generate a random byte
    print(f"{key[i]:02x}", end="")  # Print each byte as a two-digit hex value
print("\n")

# Case 2: Without using a seed for the random number generator
print("Case 2: Without using a seed:")
random.seed(None)  # This sets the seed to a default state
key = bytearray()
for i in range(KEYSIZE):
    key.append(random.randint(0, 255))  # Generate a random byte
    print(f"{key[i]:02x}", end="")  # Print each byte as a two-digit hex value
print("\n")
