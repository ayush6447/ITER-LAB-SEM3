"""a=[10,20,30,"ayush","shukla",43]
print(a)
print(a[0])
print(a[-1])
print(a[0:2])
print(a[::-1])
l=len(a)
print(l)
print(a[l-1])
i=0
while(i<l):
    print(a[i])
    i=i+1
a=[]#empty list
a.append(10)
a.append(20)
a.append(30)
print(a)
Number_of_Element=int(input("enter the number"))
Even=[]
Odd=[]
List=[]
i=0
while(i<Number_of_Element):
    Number=int(input("enter the number"))
    List.append(Number)
    if(List[i]%2==0):
        Even.append(List[i])
    else:
        Odd.append(List[i])
    i=i+1
print("Even number in the list",Even)
print("Odd number in the list",Odd)
            LINER SEARCH        """
Number_of_Element=int(input("Enter the number of elements in the list"))
List=[]
i=0
while(i<Number_of_Element):
    Elements=int(input("enter the elements"))
    List.append(Elements)
    i=i+1
Target=int(input("enter the number to be found in the list"))
i=0
flag=0
while(i<Number_of_Element):
    if(List[i]==Target):
        print("Element found at position",i+1)
        flag=1
        break
    i=i+1
if(flag==0):
    print("element not found in the list")
