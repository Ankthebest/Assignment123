size=int(input("Enter size of list :"))

lst = []

for i in range(size):
    
    elements = int(input("Input elements :"))

    lst.append(elements)

print("Input list is :",lst)


def triple_no(number):
    return 3*number
   

Triple_list=list(map(triple_no,lst))
print("Triple number list :",Triple_list)