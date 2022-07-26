l1 = ['abc', 'xyz', 'aba', '1221', "3333", "abcda"]

i = 0

for l in l1:
    length = len(l)

    if l[0] == l[length - 1]:
        i = i + 1

if i == 0:
    print("No equal characters found")
else:
    print("Output :", i)
