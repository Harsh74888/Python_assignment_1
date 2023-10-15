# to genrate a prime number from 1 to N 
def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

N = int(input("Enter the upper limit (N): "))

prime_numbers = generate_primes(N)

print(f"Prime numbers from 1 to {N}:")
print(prime_numbers)
