with open("ans.txt","r") as f_1:
    with open("ans_1.txt", "r") as f_2:
        for a,b in zip(f_1,f_2):
           
            print(a+b)