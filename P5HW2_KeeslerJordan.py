import random

#
def addRandom():
    n1=random.randint(0,1000)
    n2=random.randint(0,1000)
    print(f'{n1:>6}')
    print(f'+{n2:>5}')
    print('Enter answer')
    ans=int(input())
    while ans!=n1+n2:
        if ans<n1+n2:
            print('Sorry, guess is too low.')
        else:
            print('Sorry, guess is too high.')
        ans=int(input('try again:'))
    print('Nice.. You got it right...')

def subRandom():
    n1=random.randint(0,1000)
    n2=random.randint(0,1000)
    print(f'{n1:>6}')
    print(f'-{n2:>5}')
    print('Enter answer')
    ans=int(input())
    while ans!=n1-n2:
        if ans<n1-n2:
            print('Sorry, guess is too low.')
        else:
            print('Sorry, guess is too high.')
        ans=int(input('try again:'))
    print('Nice.. You got it right...')
if __name__=='__main__':
    
    while 1:

        print('Welcome to Math Quiz!')
        print('MAIN MENU')
        print('--------------------------')
        print('1. Adding Random Numbers')
        print('2. Subtrcting Random Numbers')
        print('3. Exit')
        print('--------------------------')

        num =int(input('Please choose one of the menu options:'))
        if num==3:
            print('See ya next time.')
            print('Bye!!')
            break
        if num==1:
            addRandom()
        if num==2:
            subRandom()
