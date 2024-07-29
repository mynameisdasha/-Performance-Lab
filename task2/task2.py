import math
with open("file1.txt", "r", encoding='utf-8') as f:
    o=f.read()
centr=(int(o[0]),int(o[2]))
print(centr)
radius=int(o[4])
print(radius)
with open("file2.txt", "r", encoding='utf-8') as f:
    o1=f.read()
point1=(int(o1[0]),int(o1[2]))
print(point1)
point2=(int(o1[4]),int(o1[6]))
print(point2)
point3=(int(o1[8]),int(o1[10]))
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
