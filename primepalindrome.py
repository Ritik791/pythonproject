n=int(input("Enter the number:\n"))
flag=0
s=0
i=0
for i in range(2,n):
    if n%i==0:
        flag=1
        # break
if flag==1:
    print("it is not a prime")
else:
    pass
    x=n
    while x>0:
        r=x%10
        s=s*10+r
        x=x//10
    if s==n:
        print(n,"is a prime palinedrome number")
    else:
        print("it is not a prime palinedrome number")

