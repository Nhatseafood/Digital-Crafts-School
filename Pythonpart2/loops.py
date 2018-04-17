'''
# 1

for number in range(1,11):
    print(number)

#2
start = int(input('Start from: '))
end = int(input('End from: '))
for number in range(start,end + 1):
    print(number)
    
#3
for number in range(1,11):
    if number %2 != 0:
        print(number)

#4
size = 5
for i in range(size):
    print('*' * size)

#5
square = int(input("How big is the square? "))
for number in range(square):
    print('*' * square)


#6
height = int(input("height size? "))
weight = int(input("weight size? "))
for number in range(1,h+1):
    if x == 1:
        print('*' * w)
    elif x == h:
        print('*' * W)
    else:
        print('*' + ' ' * (w-2) + '*')

#7
print('   *  ')
print('  *** ')
print(' ***** ')
print('******* ')


#8
h = 4
for x in range(1,5):
    print(' ' * (h-x) + '*' * x + '*' * (x-1) + ' ' * (h-x))
'''
#9
x = range(1,11)
for y in x:
    for z in x:
    mu = y * z
    print(y,'',)

