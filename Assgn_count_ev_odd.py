lst =[]

n =int(input("Enter number of elements:"))

for i in range(0,n):
    ele=int(input())
    lst.append(ele)

print("Input series is:",lst)

count_even = 0
count_odd  = 0
for num in lst:
    if num%2==0:
        count_even = count_even + 1
    else:   
        count_odd += 1
print("The number of even no. is:",count_even)
print("The number of  odd no. is:",count_odd)