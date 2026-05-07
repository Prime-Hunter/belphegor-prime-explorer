import time
from explore import is_prime, generate_palindromic_prime

print("🚀 Pushing the limits: Searching for a 100+ digit prime (n >= 48)...")
n = 48 

while True:
    num = generate_palindromic_prime(n, "369")
    num_digits = len(str(num))
    
    # We use a higher 'k' for Miller-Rabin to be extra sure on giant numbers
    if is_prime(num, k=10):
        print(f"\n💎 LIMIT BREACHED!")
        print(f"Found a {num_digits}-digit prime at n = {n}")
        print(f"Prime: {num}")
        break
    else:
        print(f"Testing n = {n} ({num_digits} digits)... ", end='\r')
    
    n += 1
