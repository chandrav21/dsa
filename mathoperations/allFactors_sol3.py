#print all factors of a given number- solution #2

def allFactors(n: int) -> list[int]:
    factors = []
    for i in range(1, (n//2 + 1)):    # parse till half of value of n
        if n % i == 0:
            factors.append(i)
    factors.append(n)
    return factors
print(allFactors(28))
print(allFactors(15))
print(allFactors(10))

#improvised TC and SC  use the range half of n O(n/2)+1 (append n at end) = O(n)
#space complexity is O(i) i is number of factors
