import random

def is_prime(n, k=5):  # Miller-Rabin Primality Test
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False

    # Find r and d such that n - 1 = 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_belphegor_number(n_zeros):
    return int(f"1{'0' * n_zeros}666{'0' * n_zeros}1")

print("Checking the Belphegor Sequence (Optimized):")
for n in range(16): # Now we can check even further!
    num = generate_belphegor_number(n)
    status = "PRIME!" if is_prime(num) else "Composite"
    print(f"Zeros: {n:2} | Digits: {len(str(num)):2} | Result: {status}")

