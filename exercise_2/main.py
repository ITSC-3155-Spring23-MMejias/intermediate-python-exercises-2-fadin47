from time import time

ntherm = int(input('Enter a term between 15 and 35: '))
n1 = 0
n2 = 1
count = 0

time_now = time()

if ntherm <= 14 or ntherm >= 36:
  print('Please enter an integer between 15 and 35: ')

else:
   print('Fib:')
   while count < ntherm:     
      nth = n1 + n2
      n1 = n2
      n2 = nth
      count += 1
print(n1)

exct_time = time() - time_now
print(f'fib took:  {exct_time}')
