ans = "hi guys \n welcome to mashupstack"

f = open('ans.txt', 'a')
f.writelines(ans)
f.close()
 

f = open('ans.txt', 'r')
lines = f.readlines()

for x in lines :
    print(x.strip())
