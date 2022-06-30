# 求1-100的偶数的和
n=1
sum=0
while n<=100:
    if n%2==0:
        sum=sum+n
    n=n+1
print(sum)

n=0
sum=0
while n<=100:
    sum+=n
    n=n+2
print(sum)