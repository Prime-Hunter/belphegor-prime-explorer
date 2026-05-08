import sys
import math
from explore import is_prime

# Set the limit to 0 globally within the script as well
sys.set_int_max_str_digits(0)

def name_to_digits(name):
    res = ""
    for char in name.upper():
        if 'A' <= char <= 'Z':
            res += f"{ord(char) - 64:02}"
        elif char == " ":
            res += "00"
    return res

name = input("Enter name or phrase: ")
name_seq = name_to_digits(name)
name_len = len(name_seq)
print(f"Target sequence: {name_seq}")

n = 0
print(f"🔍 TITAN HUNT: Searching for '{name}' prime...")

while True:
    # Build candidate mathematically to avoid string conversion issues
    # 1 * 10^(2n + name_len + 1) + int(name_seq) * 10^(n + 1) + 1
    candidate = (10**(2*n + name_len + 1)) + (int(name_seq) * 10**(n + 1)) + 1
    
    if is_prime(candidate, k=10):
        # Only convert to string at the VERY end when we find it
        sys.set_int_max_str_digits(0)
        result = f"\n💎 TITAN FOUND: {name}\nn={n}\nPrime: {candidate}\n"
        print(result)
        with open("name_primes.txt", "a") as f:
            f.write(result)
        break
    
    if n % 50 == 0:
        # Calculate digit count mathematically to avoid ValueError
        digit_count = 2*n + name_len + 2
        print(f"Testing n={n} (~{digit_count} digits)...", end='\r')
    n += 1
