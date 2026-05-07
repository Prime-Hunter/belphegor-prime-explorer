import time
import csv
from explore import is_prime, generate_belphegor_number

results = []
print(f"{'Zeros (n)':<10} | {'Time (s)':<15} | {'Result'}")
print("-" * 40)

for n in range(31):
    num = generate_belphegor_number(n)
    start = time.perf_counter()
    is_prime(num)
    end = time.perf_counter()
    duration = end - start
    res_str = "PRIME" if is_prime(num) else "Comp"
    
    print(f"{n:<10} | {duration:<15.8f} | {res_str}")
    results.append([n, duration, res_str])

# Save to CSV for external use
with open('complexity_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['n_zeros', 'time_seconds', 'is_prime'])
    writer.writerows(results)

print("\nResults also saved to 'complexity_data.csv'")
