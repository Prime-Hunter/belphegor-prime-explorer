from explore import is_prime, generate_palindromic_prime

print("Hunting for primes in the Tesla 369 sequence (1[0...0]369[0...0]1)...")
# We'll check the first 50 levels
for n in range(51):
    num = generate_palindromic_prime(n, "369")
    if is_prime(num):
        print(f"n = {n:2} | PRIME FOUND: {num}")
    elif n % 10 == 0:
        print(f"Checked up to n = {n}...")

print("\nHunt complete.")
