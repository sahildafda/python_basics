l1 = ['abc', 'xyz', 'aba', '1221', "3333", "abcda", "abc", "1221"]

# shortcut -> print(list(set(l1)))

l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)