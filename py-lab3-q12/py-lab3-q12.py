ans = ["python","java","Css","HTML"]


with open('ans.txt', "w") as myfile:
        for x in ans:
                myfile.write("%s\n" % x)

with open("ans.txt" , "r")as seen:

       print(seen.read())
