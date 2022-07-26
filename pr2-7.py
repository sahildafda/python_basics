#string reverse

s = input("Enter string here : ")

revstring = ""

i = len(s) - 1

while i >= 0:
    revstring = revstring + s[i]

    i = i - 1

print(revstring)
