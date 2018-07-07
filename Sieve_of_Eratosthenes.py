N = 10000

Li = [i for i in range(2, N + 1)]
primes = []

while Li != []:
    prime_k = Li[0]
    primes.append(prime_k)
    multiples_k = [prime_k * i for i in range(1, N // prime_k + 1)]
    Li = set(Li) - set(multiples_k)
    Li = sorted(list(Li))

print(primes)
