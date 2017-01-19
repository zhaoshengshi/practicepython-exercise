import random

CHOICES = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
RESULTS = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]

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
    r = RESULTS[c-1][s-1]
    if r == 0:
        print('HaHa, no one wins!')
    elif r == -1:
        print('You\'re %s, I\'m %s, I win!' % (CHOICES[c], CHOICES[s]))
    else:
        print('You\'re %s, I\'m %s, You win!' % (CHOICES[c], CHOICES[s]))

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

