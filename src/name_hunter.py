import sys
import os
from explore import is_prime

sys.set_int_max_str_digits(0)
CHECKPOINT_FILE = "checkpoint_amanda.txt"

def name_to_digits(name):
    res = ""
    for char in name.upper():
        if 'A' <= char <= 'Z': res += f"{ord(char) - 64:02}"
        elif char == " ": res += "00"
    return res

def load_checkpoint():
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, "r") as f:
            return int(f.read().strip())
    return 0

def save_checkpoint(n):
    with open(CHECKPOINT_FILE, "w") as f:
        f.write(str(n))

name = input("Enter name: ")
name_seq = name_to_digits(name)
name_len = len(name_seq)

# Load existing progress or start at 0
n = load_checkpoint()
print(f"🚀 Resuming '{name}' Titan hunt from n={n}...")

while True:
    candidate = (10**(2*n + name_len + 1)) + (int(name_seq) * 10**(n + 1)) + 1
    if is_prime(candidate, k=10):
        result = f"\n💎 TITAN FOUND: {name}\nn={n}\nPrime: {candidate}\n"
        print(result)
        with open("name_primes.txt", "a") as f: f.write(result)
        if os.path.exists(CHECKPOINT_FILE): os.remove(CHECKPOINT_FILE)
        break
    
    # Save progress every 100 steps
    if n % 100 == 0:
        save_checkpoint(n)
        digit_count = 2*n + name_len + 2
        print(f"Testing n={n} (~{digit_count} digits)... Checkpoint saved.", end='\r')
    n += 1
