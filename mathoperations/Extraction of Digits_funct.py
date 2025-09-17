def extract_digits(n: int) -> int:
    num = n
    if num == 0:
        return 1
    count = 0
    while num > 0:
        remainder = num % 10
        count += 1
        print("Extracting digit:", remainder)
        num = num // 10
    print("Total digits extracted:", count)



answer = extract_digits(5874)
print("Number of digits in 5874:", answer)
