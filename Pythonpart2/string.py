'''

# 1
name = "Nhat"
print(name.upper())

# 2
name = "nhat"
print(name.capitalize())


# 3
name = "Nhat"
print(name[::-1])

#4
paragraph = "Hello my name is Nhat".upper()
leet = ''
for i in paragraph:
    if i == "A":
        leet += '4'
    elif i == "E":
        leet += '3'
    elif i == "G":
        leet += '6'
    elif i == "I":
        leet += '1'
    elif i == "O":
        leet += '0'
    elif i == "S":
        leet += '5'
    elif i == "T":
        leet += '7'
    else:
        leet += i
print(leet)

'''
#5 
name = "good"
p = ''
for x in range(len(name)):
    if name[x] == p:
        name = name [:x] + 3 * name[x] + name[x:]
        x += 4
        p = name[x]
    else:
        p = name[x]
print(name)