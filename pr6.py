#to find the interest
#formula : i = p*r*n / 100

p = int(input("Enter Price Amount : "))
r = int(input("Enter Rate of Interest : "))
n = int(input("Enter Number of Years : "))

i = (p * r * n) / 100

print("Simple Interest of Given Value is : " + str(i))