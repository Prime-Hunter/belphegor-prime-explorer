import sys
from explore import is_prime

sys.set_int_max_str_digits(0)

def count_goldbach_partitions(n):
    count = 0
    # We only need to check up to n/2
    for i in range(3, n // 2 + 1, 2):
        if is_prime(i) and is_prime(n - i):
            count += 1
    return count

print("🌌 TITAN COMET GENERATOR")
start = int(input("Enter starting even number: "))
end = int(input("Enter ending even number: "))
step = int(input("Step size (even): "))

with open("titan_comet_data.csv", "w") as f:
    f.write("even_number,partition_count\n")
    for num in range(start, end + 1, step):
        if num % 2 == 0:
            c = count_goldbach_partitions(num)
            f.write(f"{num},{c}\n")
            print(f"Processed {num}: {c} partitions", end='\r')

print("\n✅ Comet data saved to titan_comet_data.csv")
