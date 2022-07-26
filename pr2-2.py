string = input("Enter String : ")

length = len(string)

if length < 2:
    print("String Empty....")

else:
    i = length
    print(string[0], string[1], string[i - 2], string[i - 1])