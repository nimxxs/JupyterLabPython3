def findMax(a, b, c):
    max = 0
    if max <= a: max = a
    if max <= b: max = b
    if max <= c: max = c
    
    return max

def findMin(a, b, c):
    min = 99999999
    if min >= a: min = a
    if min >= b: min = b
    if min >= c: min = c
    
    return min

def findSum(a, b, c):
    sum = 0
    sum += a
    sum += b
    sum += c
    
    return sum

def findPrime(x, y):
    primes = []
    for num in range(x, y+1):
        isPrime = True
        for j in range(2, num):
            if num % j == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(num)

    return primes, len(primes)