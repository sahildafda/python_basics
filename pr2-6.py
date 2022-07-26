s = input("Enter string here : ")

length = len(s)

if length == 0:
    print("Write something in string")

else:
    removechar = int(input("Enter location of char to remove : "))

    if (removechar - 1) < 0 or (removechar - 1) >= length:
        print("Enter valid location")

    else:
        s = s.replace(s[removechar - 1], "")

        print(s)