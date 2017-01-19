import random

def ask():
    while True:
        s = input('Let\'s play the game:\n\t1. Rock\n\t2. Paper\n\t3. Scissors?\nWhat you choose?: ')
        if s.isdigit():
            c = int(s)
            if not (1 <= c <= 3):
                print('Invalid input, please re-select again!')
                continue
        else:
            print('Invalid input, please re-select again!')
            continue
        return c

def ai():
    return random.randint(1, 3)

def compete(c, s):
    if s == c:
        print('HaHa, no one wins!')
    elif c == 1:
        if s == 2:
            print('I\'m Paper, I win!')
        else:
            print('I\'m Scissors, You win!')
    elif c == 2:
        if s == 1:
            print('I\'m Rock, You win!')
        else:
            print('I\'m Scissors, I win!')
    elif c == 3:
        if s == 1:
            print('I\'m Rock, I win!')
        else:
            print('I\'m Paper, You win!')

def another():
    while True:
        ans = input('Another round? y/n: ')
        if ans == 'y':
            return True
        elif ans == 'n':
            return False
        else:
            print('Invalid input, try again!')
            continue

if __name__ == '__main__':
    while True:
        c = ask()
        a = ai()
        compete(c, a)
        if not another():
            break

