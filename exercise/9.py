import random

i = random.randint(1, 9)

def ask_for_input():
    while True:
        s = input('Please guess what I got (an integer between 1 and 9) in hand?: ' )
        ii = int(s)
        if 1 <= ii <= 9:
            return ii
        else:
            print('Wrong input!')
            continue

def ask_for_again():
    while True:
        s = input('Wanna try again? (y)es or (e)xit : ')
        if s == 'y':
            return True
        elif  s == 'e':
            return False
        else:
            print('Wrong input!')
            continue

if __name__ == '__main__':
    while True:
        a = ask_for_input()
        if a == i:
            print('You got it right, it is %s' % a)
            break
        else:
            print('Sorry, it\'s not right!')
            r = ask_for_again()
            if not r:
                break

