import sys
import ccard
import random

choice = input('[+] CC Gen : ')
month = str(random.randint(1, 30))
year = str(random.randint(2024, 2030))

def gen():
    f = open('./db/cc.txt', 'a+')
    if choice == 'visa' or 'VISA':
        x = ccard.visa()
        f.write('\n' + f'{x}' + '|' + f'{month}' + '|' + f'{year}')
        f.close()

gen()
if __name__ == '__main__':
  ask = input('Again? [y/n] > ')
  if ask == 'y':
    gen()
  else:
    sys.exit(0)
