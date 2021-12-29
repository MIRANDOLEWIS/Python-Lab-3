import random
lines = open('ans.txt',"r")

x = lines.read().splitlines()

myline =random.choice(x)
print(myline)