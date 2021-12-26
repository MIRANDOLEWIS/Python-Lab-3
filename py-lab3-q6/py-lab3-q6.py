list = ["jerin\n","ajay\n","deepak\n"]

f = open('ans.txt', 'a')
f.writelines(list)
f.close()
 

f = open('ans.txt', 'r')
lines = f.readlines()

for x in lines :
    print(x.strip())
