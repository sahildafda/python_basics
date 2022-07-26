s = input("Enter string here : ")

length = len(s)

if length < 3:
    print(s)

else:
    if s[length - 3:] == "ing":
        s = s + "ly"

    else:
        s = s + "ing"

    print(s)