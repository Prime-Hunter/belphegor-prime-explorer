from explore import is_prime
import sys

def verify_prime(n):
    print(f"--- Hard Verification for: {str(n)[:20]}... ({len(str(n))} digits) ---")
    
    # Step 1: Trial division with small primes
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for p in small_primes:
        if n % p == 0 and n != p:
            return False, f"Failed: Divisible by {p}"

    # Step 2: High-accuracy Miller-Rabin (k=50)
    # The chance of a composite number passing 50 tests is less than 1 in 2^100
    if is_prime(n, k=50):
        return True, "Verified: Confirmed Prime with high confidence."
    else:
        return False, "Failed: Fails high-accuracy Miller-Rabin test."

if __name__ == "__main__":
    try:
        val = int(input("Enter the number to verify: "))
        success, msg = verify_prime(val)
        print(msg)
    except ValueError:
        print("Invalid input. Please enter a number.")
