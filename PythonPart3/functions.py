import matplotlib.pyplot as plotlibrary
import math
from numpy import arange
'''

#1. hello
def hello(x):
    print("Hello " + x)

hello('Igor')

1.2
def hello(name):
     print("Hello" + name)

hello(" Nhat")   

#2. y = x + 1
import matplotlib.pyplot as plotlibrary

def f(x):
    return x + 1

xs = list(range(-3 ,3))
ys = []
for x in xs:
    ys.append(f(x))

plotlibrary.plot(xs, ys)
plotlibrary.show()


# 3. Square of x
import matplotlib.pyplot as plotlibrary

def f(x):
    return x**2

xs = list(range(-100, 100))
ys = []
for x in xs:
    ys.append(f(x))

plotlibrary.plot(xs,ys)
plotlibrary.show()


# 4. odd or even
import matplotlib.pyplot as plotlibrary

def f(x):
    if x % 2 == 0:
        return -1
    else:
        return 1

xs = list(range(-5, 5))
ys = []

for x in xs:
    ys.append(f(x))

plotlibrary.bar(xs, ys)
plotlibrary.show()


# 5. Sine
import matplotlib.pyplot as plotlibrary
import math

def f(x):
    return math.sin(x)

xs = list(range(-5, 5))
ys = []

for x in xs:
    ys.append(f(x))

plotlibrary.plot(xs, ys)
plotlibrary.show() 


# 6. Sine 2
import matplotlib.pyplot as plotlibrary
import math
from numpy import arange

def f(x):
    return math.sin(x)

xs = arange(-5, 6, 0.1)
ys = []

for x in xs:
    ys.append(f(x))

plotlibrary.plot(xs,ys)
plotlibrary.show()


# 7. degree conversion

def f(tempc):
    return tempc * 1.8 + 32

xs = list(range(-2, 2))
ys = []

for tempc in xs:
    ys.append(f(tempc))
    
plotlibrary.plot(xs, ys)
plotlibrary.show()

# 8 play again
def f():
    answer = input("Do you want to play again (Y or N)? ")
    if answer == 'Y':
        return True
    else:
        return False
f()



# 9
def f():
    answer = input("Do you want to play again (Y or N)? ")
    if answer == 'Y':
        return True
    elif answer == 'N':
        return False
    else:
        print("invalid input. Please try again. ")
        f()   
f()


