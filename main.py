print(('MERRY CHRISTMAS').center(30))
print('\n \n')


z = 15
x = 1
for i in range(16):
  if i%2==0:
        print(' ' * z + '*' * x + ' ' * z)
  
  else:
        print(' ' * z + '^' * x + ' ' * z)
  x+=2
  z-=1
for j in range(3):
    print(('HHHHHHHH').center(30))
