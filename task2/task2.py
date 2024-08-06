import math
n=str(input())
m=str(input())
with open(n, "r", encoding='utf-8') as f:
    o=f.read()
wo=str(o)
normal_string = wo.replace('\n', ' ')
numb=normal_string.split()
int_numb=[int(num) for num in numb]
centr=(int_numb[0],int_numb[1])
radius=int_numb[2]
with open(m, "r", encoding='utf-8') as f:
    o1=f.read()
wo1=str(o1)
normal_string1 = wo1.replace('\n', ' ')
numb1=normal_string1.split()
int_numb1=[int(num) for num in numb1]
point=[0]*(len(int_numb1)//2)
j=0
while j<(len(int_numb1)//2):
    for i in range (0,len(int_numb1)-1,2):
        point[j]=(int_numb1[i],int_numb1[i+1])
        j+=1
def func(centr,radius,point):
    if (math.dist(point, centr) < radius):
        return 1
    if (math.dist(point, centr) == radius):
        return 0
    if (math.dist(point, centr) > radius):
        return 2
polozheniya=[0]*len(point)
for j in range (0,len(point)):
    polozheniya[j]=func(centr,radius,point[j])
for j in range (0,len(point)):
    print(polozheniya[j])
