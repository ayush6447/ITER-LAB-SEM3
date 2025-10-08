'''Number_of_Element=int(input("Enter the number of elements in the list"))
List=[]
i=0
while(i<Number_of_Element):
    Elements=int(input("enter the elements"))
    List.append(Elements)
    i=i+1
Target=int(input("enter the number to be found in the list"))
i=0     
flag=0
List.sort()
while(i<Number_of_Element):
    mid=(i+Number_of_Element)//2
    if(Target==List[mid]):
        print("number found")
        flag=1
        break
    elif(Target>List[mid]):
        i=mid+1
    else:
        Number_of_Element=mid-1
if(flag==0):
    print("number not found")
Number_of_Element=int(input("Enter the number of elements in the list"))
List=[]
min=0
i=0
while(i<Number_of_Element):
    Elements=int(input("enter the elements"))
    List.append(Elements)
    i=i+1
max=List[0]
min=List[0]
for i in range(0,i<Number_of_Element,i++):
    if(List[i]>max):
        max=List[i]
    elif(List[i]<min):
        min=List[i]
print("Maximun element in the list",max)
print("Mininmun element in the list",min)'''
a=[1,2,3,4,5]
b=[2,3,4,5,6]
for i in range(0,5):
    print(a[i]+b[i],end=' ')
