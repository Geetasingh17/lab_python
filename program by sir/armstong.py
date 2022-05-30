num=int(input("enter no "))
sum=0
temp=num

while(temp>0):
          rem=temp%10
          sum +=rem ** 3
          temp //= 10

if(num==sum):print("armstrong")
else: print("not")    
