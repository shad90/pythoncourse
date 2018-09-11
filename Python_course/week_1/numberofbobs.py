#Number of bobs in string
s = input("Input String Here: ")
index = 0
count = 0
while (index+2) < len(s):
    if s[index] == 'b':
        if s[index:index+3] == 'bob':
            count += 1
    index += 1
print("Number of times bob occurs is:",count)
