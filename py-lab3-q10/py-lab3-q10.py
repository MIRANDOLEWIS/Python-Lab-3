import collections

with open("ans.txt" , "r") as see:

   
    ans = collections.Counter(see.read())

    for x,y in ans.items():

     print(x,"repeat",y,"times")

    see.close()