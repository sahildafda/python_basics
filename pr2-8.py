s = input("Enter string here : ")

length = len(s)
evenstring = ""

i = 0

while i < length:
    if i % 2 == 0:
        evenstring = evenstring + s[i]

    i = i + 1

print(evenstring)