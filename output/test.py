n=str(input(""))
b=len(n)
str=""
for i in range(0,b):
    if n[i].isupper():
     str+=n[i].lower()
    else:
     str+=n[i].upper()
    print(str)

         
