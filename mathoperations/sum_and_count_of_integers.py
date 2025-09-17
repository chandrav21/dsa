#number count in integer.
n = 5873
num = n
sum = 0 
count = 0
while num > 0:
    sum = sum + (num % 10)
    num = num // 10
    count = count + 1
print("Sum of digits in ", n, " is ", sum)
print("Count of digits in ", n, " is ", count)
