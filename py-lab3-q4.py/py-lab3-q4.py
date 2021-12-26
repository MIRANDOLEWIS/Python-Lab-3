def lastline(f,n):
    with open(f) as file:
        print("last",n,"lines from files : ",f)
        for line in (file.readlines()[-n:]):
            print(line,end="")

name = input("enter your name :")
num = int(input("enter the number of line : ")) 

          
lastline(name,num)
