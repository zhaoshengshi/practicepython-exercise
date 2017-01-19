num = int(input('Please give me a number: '))
print([i for i in range(1, num) if not (num % i)])
