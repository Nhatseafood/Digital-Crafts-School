#challenge 
number = list(range(1,1001))
for i in number:
    if i%3 == 0 and i%5 == 0:
        print("Fizzbuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        pass
'''
#challenge
number = list(range(1,1001))
sum = 0
for i in number:
    if i%3 ==0 or i%5 == 0:
        sum += i
        print(sum)     