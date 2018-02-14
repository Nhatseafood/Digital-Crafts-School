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
'''
#5
square = int(input("How big is the square? "))
for number in range(square):
    print('*' * square)