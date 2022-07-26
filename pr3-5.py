s1 = input("Enter string : ")
n = int(input("Enter N : "))

l1 = s1.split()
l2 = []

for l in l1:
    if len(l) > n:
        l2.append(l)

print(l2)