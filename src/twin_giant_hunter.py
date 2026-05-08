from explore import is_prime, generate_palindromic_prime
import time

n = 48
with open("twin_discovery.txt", "a") as f:
    f.write(f"--- Hunt started at {time.ctime()} ---\n")

print("🎯 THE SAFE TWIN HUNT: Saving results to 'twin_discovery.txt'...")

while True:
    p = generate_palindromic_prime(n, "369")
    if is_prime(p, k=10):
        if is_prime(p + 2, k=10):
            result = f"\n🌟 TWIN GIANT FOUND!\nn = {n} | Digits: {len(str(p))}\nP: {p}\nP+2: {p+2}\n"
            print(result)
            with open("twin_discovery.txt", "a") as f:
                f.write(result)
            break
    n += 1
    if n % 50 == 0:
        print(f"Still hunting... reached n={n}", end='\r')
