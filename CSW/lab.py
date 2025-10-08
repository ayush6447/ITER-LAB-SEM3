'''print("hello world")
i=1
for i in range(0,5):
     print("Hello")
   '''
'''                 
a=1200
print(type(a))
print("iterview\nyoyo")
b=232
x=123
print(2)
name="ayush"
b,n,m='iter',234,789
print(name)
print(b,n,m)    
print(type(b))
h=1
y=float(h)
print(y)
print(type(y))
k=int(y)
print(k)
print(type(k))

#function
def ak(a,k):
 
 print(a)
 print(k)
ak(a,k)#function called 

print(a==b)
print(bool(-2))

print(a%232)
j=100
print(j==0|k==0)

'''
'''#Q2
name = "ayush"
email="ayush@apple.com"
print(name)
print(email)
#Q1
a=12
b=45
c=a+b
d=a-b
e=a*b
f=a**b
g=a/b
h=a%b
i=a//b
print(c,d,e,f,g,h,i)

a,b=b,a'''
'''
a=5
b=6
c=8

if a>b and b>c:
    print("a is greater")
elif a<b and b>c:
    print("b is greater")
else:
    print("c is greater")


#print("b is greater") if a>b else  print("a is greater")

qty= int(input("enter no"))
price= int(input("enter no"))
print(qty)
if qty>1000:
      dis=10
else:
      dis=0
total = qty*price-dis*qty*price/100


sum=qty+5
print(sum)

'''


'''
salary=input("enter salary :")
print("first salary =",salary)
if salary<=1500:
    hra=0
    da=
else:
    hra=0.10*salary
    da=0.90*salary

gross=salary+hra+da  
'''
'''day=5
match day:
    case 1|2|3|4|5:
        print("monday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("enter the no between 1 to 7 bitch")'''


'''a = 12
b = 45

op=int(input("enter operation 1 to 7"))
match op:
    case 1:
        c = a + b
        print("Add:", c)
    case 2:
        d = a - b
        print("Sub:", d)
    case 3:
        e = a * b
        print("Multiply:", e)
    case 4:
        f = a ** b
        print("Power:", f)
    case 5:
        g = a / b
        print("Div:", g)
    case 6:
        h = a % b
        print("Mod:", h)
    case 7:
        i = a // b
        print("Floor Division:", i)
'''
'''a=3
i=10
while(i>0):
    i=i-1
    a=a+a
    print(a)
    if i==2:
        continue
'''

'''for i in range(1,20,2):
    print(i)
a=0  
while a>20:
    a=a+2           
    print(a)   
''''''
s = "bbsr-751030"
alp = 0
dig = 0

for i in s:
    if i.isalpha():
        alp += 1
    elif i.isdigit():
        dig += 1

print("Alphabets:", alp)
print("Digits:", dig)
'''
'''
def main():
    for i in range(5):
        print("hello")
if __name__ == "__main__":
    main()
'''
'''def add(fname,a,b):
    print(fname.upper())
    print(a+b)
add(fname="ayush",a=12,b=45)
add(fname="ash",a=1,b=4)
add(fname="sh",a=2,b=5)
add(fname="h",a=126,b=456)
add(fname="a",a=125,b=458)
add(fname="ay",a=127,b=45465)
add(fname="ayu",a=1232,b=4565)
'''





'''def calc(a, b, c, op):
    if op == "sum":
        return a + b + c
    elif op == "product":
        return a * b * c
    else:
        return None

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))
op = input("Enter operation (sum/product): ").strip().lower()

result = calc(num1, num2, num3, op)

if result is not None:
    print(f"{op.capitalize()} of three numbers =", result)
else:
    print("Invalid operation")'''
'''
# Factorial of a number

n = int(input("Enter a non-negative integer: "))



def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result


print(f"Factorial of {n} is {factorial(n)}")
r=input("enter rdius")
print(f"area={3.14*int(r)**2}")
'''



numbers = []


i = 1  

while i <= 10: 
    numbers.append(i)  
    i += 1             

print("The list is:", numbers)




tb=("a","b",1)
print(tb[2])