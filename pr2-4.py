s1 = input("Enter First string here : ")
s2 = input("Enter Second string here : ")

tmp = s1

if len(s1) < 2 or len(s2) < 2:
    print("Enter some big string")

else:
    s1 = s1.replace(s1[0], s2[0])
    s1 = s1.replace(s1[1], s2[1])

    s2 = s2.replace(s2[0], tmp[0])
    s2 = s2.replace(s2[1], tmp[1])

    combination = s1 + " " + s2
    print(combination)