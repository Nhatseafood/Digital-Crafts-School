'''
#sum
number = [2, 4, 6]
print(sum(number))

#largestnum
number = [1, 2, 3, 100]
print(max(number))

#smallestnum
number = [4, 5, 6, 7]
print(min(number))


#evennumbers
a = [1, 2, 3, 4]
for number in a:
    if number %2 ==0:
        print(number)


# 5
a = [1, 2, 3, 4, 5]
for i in a:
    if i > 0:
        print(i)   

#6
a = [1, 2, 3, 4, 5]
b=[]
for i in a:
    if i > 0:
        b.extend([i])

print(b)     
   
#7
a = [1, 2, 3, 4, 5]
c = []
for i in a:
    c.extend([i*2])

print(c)   
 
#8
a = [1, 2, 3]
b = [4, 5, 6]
d =[]

for i in a:
    d.extend([i*b[a.index(i)]])
print(d)

#9
a = [[1, 3], [2, 4]]
b = [[5, 2], [1, 0]]
c = [[],[]]

for i in a:
    y = a.index(i)
    for x in i:
        k = a[y].index(x)
        z = a[y][k] + b[y][k]
        c[y].extend([z])
print(c)
'''    
day = int(input("Pick a day number (0-6)? "))
week = ["Sun", "M", "T", "W", "Th", "F", "Sat"]
if week[day] == "Sun" or week[day] == "Sat":
    print("Sleep in")
else:
    print("Go to work")