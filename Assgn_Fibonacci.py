no = int(input("Enter a no. for fibonacci series:"))
print("Series would be entered no.+1 in length but upto value 50")
print("Fibonacci series with expectd output:")

a=0
b=1
print(b,end=' ')
for i in range(no):
    c = a + b
    if c<50:
        print(c,end= ' ')
        a = b
        b = c