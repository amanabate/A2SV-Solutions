# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def almost_primes(n):
    cnt = [0] * (n + 1)
    
    # Sieve-like process
    for p in range(2, n + 1):
        if cnt[p] == 0:  # p is prime
            for multiple in range(p, n + 1, p):
                cnt[multiple] += 1

    # Count numbers with exactly 2 distinct prime divisors
    ans = sum(1 for i in range(2, n + 1) if cnt[i] == 2)
    return ans


# Input
n = int(input())
print(almost_primes(n))