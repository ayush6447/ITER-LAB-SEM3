# Assuming 'List' is your list variable; rename to 'lst' for clarity
lst = [1,2,3,4,5,6,7,8,9]  # Replace with actual list

lst2 = [1 ,3,4,5,6,7,8,9]
max_val = lst[0]
min_val = lst[0]
for i in range(1, len(lst)):
    if lst[i] > max_val:
        max_val = lst[i]
    elif lst[i] < min_val:  
        min_val = lst[i]
    
print("Max: ",max_val, "Min:", min_val)
ab=('f','h','h','f','d')
lst[0]=ab[1]
print(lst)