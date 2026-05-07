from explore import is_prime
import time

def name_to_digits(name):
    # Converts 'ABC' to '010203'
    return "".join(f"{ord(c.upper()) - 64:02}" for c in name if c.isalpha())

name = input("Enter the name to hide: ")
name_seq = name_to_digits(name)
print(f"Target sequence for '{name}': {name_seq}")

n = 0
print("🔍 Searching for your name-prime...")
while True:
    # Pattern: 1 [zeros] [name_seq] [zeros] 1
    candidate = int(f"1{'0' * n}{name_seq}{'0' * n}1")
    if is_prime(candidate, k=10):
        print(f"\n💎 FOUND IT! Your name-prime exists at n={n}")
        print(f"The Prime: {candidate}")
        # Save discovery
        with open("name_primes.txt", "a") as f:
            f.write(f"Name: {name} | n: {n} | Prime: {candidate}\n")
        break
    
    if n % 50 == 0:
        print(f"Testing n={n} ({len(str(candidate))} digits)...", end='\r')
    n += 1
