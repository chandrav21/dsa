#print all factors of a given number- solution #2
import math 
def allFactors(n: int) -> list[int]:
    num = n
    Factors = []
    sq = int(math.sqrt(num))
    print("Square Root of", n,  "is:", sq, "will use this for max range")

    while num > 1:
        for i in range(1, sq+1):
            print("Current i value is:", i)
            if num % i == 0:
                Factors.append(i)
                if num // i != i:
                    Factors.append(num // i)
                    print("Factors found so far:", Factors)
        Factors.sort()
        return Factors

            
print(allFactors(25))
print(allFactors(15))
print(allFactors(10))



    
