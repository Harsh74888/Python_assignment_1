# display the sum of n number using list 
number=[]
n=int(input("enter the value of n:"))
for i in range(n):
    num=float(input("enter a number {} of {}:".format(i+1,n)))
    number.append(num)
    total=sum(number)
print("the sum of {} number is :{}".format(n,total))