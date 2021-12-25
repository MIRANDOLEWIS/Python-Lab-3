ans = open("ans.txt","a")
ans.write(input("Enter your Name : "))
ans.close()

ans = open("ans.txt" , "r")
print(ans.read())
