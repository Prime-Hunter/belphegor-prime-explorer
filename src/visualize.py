import time
from explore import is_prime, generate_belphegor_number

print(f"{'Zeros (n)':<10} | {'Time (seconds)':<15}")
print("-" * 30)

# We'll check up to 30 zeros
for n in range(31):
    num = generate_belphegor_number(n)
    start = time.perf_counter()
    is_prime(num)
    end = time.perf_counter()
    result = "PRIME" if is_prime(num) else "Comp"
    print(f"{n:<10} | {end - start:<15.8f} | {result}")
