# Palindromic Prime Explorer

This project explores the mathematical properties and computational complexity of specific palindromic prime families.

## Mathematical Findings

### 1. The Belphegor Sequence (Center: 666)
- **Structure**: $1[0]_n666[0]_n1$
- **Findings**: Successfully identified the **Belphegor Prime** at **n=13** (31 digits).
- **Other Primes**: Found a 'tiny' prime at **n=0** (16661).

### 2. The Seven Devils Sequence (Center: 777)
- **Structure**: $1[0]_n777[0]_n1$
- **Findings**: Identified an immediate prime at **n=0** (17771). This family shows a much higher probability of primality in its early stages compared to the 666 family.

## Computational Tools
- `src/explore.py`: A generalized engine using the **Miller-Rabin primality test** to quickly verify massive numbers.
- `src/visualize.py`: A complexity tracker that exports computational 'work' data to `complexity_data.csv`.
- `src/seven_devils.py`: A specialized hunter script for rapid sequence discovery.

## Usage
To run the general explorer:
```bash
python src/explore.py
```
