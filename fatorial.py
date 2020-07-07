n = int(input())
k = int(input())

print("o binomial é:", binomial(n, k))

def binomial (n, k):
        return fatorial(n) / fatorial(k) * fatorial(n - k)

def fatorial (n):
        if (n == 1 or n == 0):
                return 1
        else:
            f = n
            n -= 1
            while (n != 1):
                f = f * n
                n -= 1
            return f

