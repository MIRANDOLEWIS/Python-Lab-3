from itertools import islice

with open("ans.txt") as ans:

    final = list(islice(ans, 1))

print(final)