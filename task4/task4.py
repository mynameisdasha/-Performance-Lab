import math
def min_moves(nums):
    average = sum(nums) // len(nums)
    moves = 0
    for num in nums:
        moves += abs(num - average)
    return moves
m=str(input())
with open(m, "r", encoding='utf-8') as p:
    o=p.read()
wo=str(o)
normal_string = wo.replace('\n', ' ')
numb=normal_string.split()
int_numb=[int(num) for num in numb]
print(min_moves(int_numb))
