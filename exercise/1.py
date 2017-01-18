
# Exercise 1

from datetime import date

def run():
    name = input('Please tell me your name: ').title()
    age = input('Hey, %s!\nHow old are you: ' % name)

    year = 100 - int(age) + date.today().year
    #print('Thanks %s' % name + ', you will turn 100 years old in %s' % year)
    print('Thanks %s, you will trun 100 years old in %s.' % (name, year))

if __name__ == '__main__':
    run()

