#check if number is armstrong or not
def isArmstrong(n: int) -> bool:
    num = n
    sum = 0
    length = len(str(num))
    while num > 0:
        digit = num % 10 
        sum = digit ** length + sum
        num = num // 10
    if sum == n:
        return True
    return False
check = isArmstrong(153)
check1 = isArmstrong(1234)
check2 = isArmstrong(1634)
print("Is number armstrong?", check)
print("Is number armstrong?", check1)  
print("Is number armstrong?", check2) 


#TC is O(log10(n)) since its while loop with // 10 operation.
#SC is O(1) since no extra space is used.No additional data structures 
#lists, arrays or hash tables are used, input size is not changing if 
# the number of digits increase substantially(no increase in memory w.r.t input size)
