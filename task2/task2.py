import math
with open("file1.txt", "r", encoding='utf-8') as f:
    o=f.read()
wo=str(o)
normal_string = wo.replace('\n', ' ')
numb=normal_string.split()
int_numb=[int(num) for num in numb]
centr=(int_numb[0],int_numb[1])
print(centr)
radius=int_numb[2]
print(radius)
with open("file2.txt", "r", encoding='utf-8') as f:
    o1=f.read()
wo1=str(o1)
normal_string1 = wo1.replace('\n', ' ')
numb1=normal_string1.split()
int_numb1=[int(num) for num in numb1]
point1=(int_numb1[0],int_numb1[1])
print(point1)
point2=(int_numb1[2],int_numb1[3])
print(point2)
point3=(int_numb1[4],int_numb1[5])
print(point3)
def func(centr,radius,point):
    if (math.dist(point, centr) < radius):
        return 1
    if (math.dist(point, centr) == radius):
        return 0
    if (math.dist(point, centr) > radius):
        return 2
print(func(centr,radius,point1))
print(func(centr,radius,point2))
print(func(centr,radius,point3))
