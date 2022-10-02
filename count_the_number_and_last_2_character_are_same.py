# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a givenlist of strings.
count = 0

my_string = "Programiz"
my_char = "r"

for i in my_string:
    if i == my_char:
        count += 1

print(count)