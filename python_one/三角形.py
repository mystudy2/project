"""
#左对齐三角形
*
**
***
****
for i in range(1,5):
    print(i*'*')

n=0
while n<5:
    print(n*'*')
    n+=1
#左对齐倒三角形
****
***
**
*
for i in range(5):
    print((5-i)*'*')

n=5
while n>0:
    print(n*'*')
    n-=1
#右对齐倒三角形
****
 ***
  **
   *
for i in range(5):
    print(i*' ',(4-i)*'*')

n=0
while n<5:
    print(n*' ',(4-n)*'*')
    n+=1

#右对齐三角形
   *
  **
 ***
****
for i in range(1,5):
    print((4-i)*' ',i*'*')

n=1
while n<5:
    print((4-n)*' ',n*'*')
    n+=1

#正三角形
   *
  ***
 *****
*******
1 3
3 2
5 1
7 0

(8-i)//2
for i in range(0,4):
    print((3-i)*' ',(2*i+1)*'*')
for i in range (1,9,2):
    print((9-i)//2*' ',i*'*')


n=0
while n<4:
    print((3-n)*' ',(2*n+1)*'*')
    n+=1

#倒三角形
*******
 *****
  ***
   *
 1 0
 3 1
 5 2

i//2
for i in range (1,9,2):
    print((i//2)*' ',(9-i-1)*'*')

#菱形
    *
   ***
  *****
 *******
  *****
   ***
    *
for i in range (1,9,2):
    print((8-i)//2*' ',i*'*')
for i in range (1,7,2):
    print((i//2+1)*' ',(7-i-1)*'*')




w=1
while w<3:
    n=0
    while n<w:
        print(n*' ',end='')
        n+=1
    n1=5
    while n1>=2*w-1:
        print('*',end='')
        n1-=1
    print()
    w+=1
"""


