# How Do You Check The Presence Of A Key In A Dictionary?
def checkKey(dic, key):
     
    if key in dic:
        print("Present, ", end =" ")
        print("value =", dic[key])
    else:
        print("Not present")
 
dic = {'a': 100, 'b':200, 'c':300}
key = 'a'
checkKey(dic, key)
 
key = 'l'
checkKey(dic, key)