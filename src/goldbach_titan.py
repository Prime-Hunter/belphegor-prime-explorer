import sys
from explore import is_prime

# Lifting the limit for our "Limit Pusher" student
sys.set_int_max_str_digits(0)

def find_goldbach_pair(even_num):
    if even_num <= 2 or even_num % 2 != 0:
        return None, "Must be an even number greater than 2."
    
    # We check from the smallest primes upward
    # For massive numbers, the first prime is often very small
    test_p = 3
    while test_p < even_num // 2:
        if is_prime(test_p):
            if is_prime(even_num - test_p):
                return (test_p, even_num - test_p), None
        test_p += 2
    return None, "No pair found (this would disprove the conjecture!)"

if __name__ == "__main__":
    try:
        val = int(input("Enter a massive even number to test: "))
        pair, error = find_goldbach_pair(val)
        if pair:
            print(f"✅ GOLDBACH VERIFIED!")
            print(f"{val} = {pair[0]} + {pair[1]}")
        else:
            print(error)
    except ValueError:
        print("Invalid input.")
