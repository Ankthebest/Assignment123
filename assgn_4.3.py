size=int(input("Enter size of list :"))

lst = []

for i in range(size):
    
    elements = int(input("Input elements :"))

    lst.append(elements)

print("Input list is :",lst)



def square_no(number):
    return number**2
   

Square_list=list(map(square_no,lst))
print("Square number list :",Square_list)