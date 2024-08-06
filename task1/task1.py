from collections import deque
n,m=int(input()),int(input())
t=0
buffer=deque()
a=deque()
b=deque()
d=deque()
for i in range (1, n+1):
    buffer.append(i)
for i in range (0, m):
    a.append(buffer[i])
k=buffer[0]
u=0
while (a[m-1]!=k):
    d=a
    d.pop()
    for j in range (0,m-1):
        buffer.append(d[j])
    while (u<m-1):
        buffer.popleft()
        u+=1
    b.append(a[0])
    a.clear()
    u=0
    for j in range (t,m):
        a.append(buffer[j])
d=a
d.pop()
for j in range (0,m-1):
    buffer.append(d[j])
while (u<m-1):
    buffer.popleft()
    u+=1
b.append(a[0])
a.clear()
u=0
for j in range (t,m):
    a.append(buffer[j])
chislo = int(''.join((str(i) for i in b)))
print(chislo)
