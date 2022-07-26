s = input("Enter string here : ")

changing = s[0]

newstring = s.replace(changing, "@")
newstring = changing + newstring[1:]

print(newstring)