import ccard
import random
import sys
#UTF-8 ENCODE

month = str(random.randint(1, 12))
year = str(random.randint(2024, 2030))
choice = input("Enter Card Type: ")

def gen():
  if choice == "visa" or "VISA":
    x = ccard.visa()
    print(f"{x} | {month} | {year}")
    
gen()
try:
  while True:
    if __name__ == "__main__":
      ask = input("Again? [y/n] >> ")
      if ask  == 'y':
        gen()
except:
  sys.exit()
  pass
