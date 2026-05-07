from explore import is_prime, generate_palindromic_prime

print("Hunting for the first prime in the 777 sequence (1[0...0]777[0...0]1)...")
n = 0
while True:
    num = generate_palindromic_prime(n, "777")
    if is_prime(num):
        print(f"\nSUCCESS! Found a prime at n = {n} zeros.")
        print(f"The prime is: {num}")
        break
    else:
        # Print progress every 5 zeros to show it's working
        if n % 5 == 0:
            print(f"Checked up to n = {n}...", end='\r')
    n += 1
