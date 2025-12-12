import math
import re

with open("input2.txt", 'r') as f:
    lines = [line.rstrip('\n') for line in f]

ranges = lines[0].split(",")

tups = [[int(tup) for tup in ranger.split("-")] for ranger in ranges]
strups = [ranger.split("-") for ranger in ranges]
lups = [[len(tup) for tup in ranger.split("-")] for ranger in ranges]
tot = 0
usefulRanges = []

# def roundUp(tup1):
#     tenPow = 10**(math.ceil(math.log10(tup1)) // 2)
#     first1, second1 = tup1 // tenPow, tup1 % tenPow
#     if first1 < second1:
#         return (first1 + 1)*(tenPow + 1)
#     else:
#         return (first1)*(tenPow + 1)

# def roundDown(tup2):
#     tenPow = 10**(math.ceil(math.log10(tup1)) // 2)
#     first2, second2 = tup2 // tenPow, tup2 % tenPow
#     if first2 < second2:
#         return (first2)*(tenPow + 1)
#     else:
#         return (first2 - 1)*(tenPow + 1)
tups = sorted(tups, key=lambda x: x[1])
smallest = tups[0][0]
largest = tups[-1][-1]
print(smallest, largest)
for start, finish in tups:
    for i in range(start, finish + 1):
        if re.match(r'^(\d+)\1+$', str(i)):
            tot += i
print(tot)




# """
# 1. Find even lengths between lengths of numbers
# 2. for each even number length, find what things of form abcabc there are
# 3. sum them?
# """
