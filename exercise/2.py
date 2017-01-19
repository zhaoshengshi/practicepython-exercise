
dividend = int(input('Please give me a dividend: '))
divisor = int(input('Please give me a divisor: '))

remainder = dividend % divisor
if remainder:
    print('%s cannot be divided evenly by %s.' % (dividend, divisor))
else:
    print('%s can be divided evenly by %s.' % (dividend, divisor))


