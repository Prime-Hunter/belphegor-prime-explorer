import random

def is_prime(n, k=5):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True

def generate_palindromic_prime(n_zeros, center):
    return int(f"1{'0' * n_zeros}{center}{'0' * n_zeros}1")

def check_sequence(center, limit=20):
    print(f"\nChecking Sequence for Center: {center}")
    print("-" * 30)
    for n in range(limit):
        num = generate_palindromic_prime(n, center)
        if is_prime(num):
            print(f"Zeros: {n:2} | PRIME FOUND: {num}")

# Explore both families
check_sequence("666", limit=15)
check_sequence("777", limit=15)
