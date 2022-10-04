# Write a Python program to find the highest 3 values in a dictionary
from heapq import nlargest
d = {'1':500, '2':5874, '3': 560,'4':400, '5':5874, '6': 20}  
three_largest = nlargest(3, d, key= d.get)
print(three_largest) 
