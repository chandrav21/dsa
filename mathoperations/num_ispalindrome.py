# check if number is palindrome or not 
# without  string conversion as number will be in integer format
def isPalindrome(n: int) -> bool:
    num = n
    reverse_num = 0
    while num > 0:
        digit = num % 10
        reverse_num = reverse_num * 10 + digit
        num = num // 10
    if reverse_num == n:
        return True
    return False
check = isPalindrome(121)
check1 = isPalindrome(124521)
print("Is number palindrome?", check)
print("Is number palindrome?", check1)
