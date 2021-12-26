list = ["jerin\n","ajay\n","deepak\n"]

f = open('myfile.txt', 'a')
f.writelines(list)
f.close()
 

f = open('myfile.txt', 'r')
lines = f.readlines()

for x in lines :
    print(x.strip())
