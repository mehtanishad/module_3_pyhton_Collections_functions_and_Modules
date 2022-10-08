# Write a Python program to create a dictionary from a string.
str = input('enter a string: ')
dic={}
for ch in str:
    if ch in dic:
        dic[ch] += 1
else:
    dic = 1
    print(dic)


