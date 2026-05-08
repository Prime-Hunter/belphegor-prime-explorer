import random

# Pre-computed small primes to speed up filtering
SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def is_prime(n, k=5):
    if n < 2: return False
    # Quick trial division
    for p in SMALL_PRIMES:
        if n % p == 0: return n == p
    
    # Fast Miller-Rabin for the survivors
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
