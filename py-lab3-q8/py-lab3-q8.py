def longest_word(filename):
        file = open(filename,"r")
        words = file.read().split() 
     
        max_len = len(max(words,key = len))
        for x in words :
              if len(x)== max_len :
                 print(x)

longest_word('ans.txt')
