ss = input('Please give me a string: ')

if ss == ss[::-1]:
    print("Yes, %s is a palindrome." % ss)
else:
    print('Nevermind, %s isn\'t a palindrome.' % ss)
