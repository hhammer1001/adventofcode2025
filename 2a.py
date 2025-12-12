import math

with open("input2.txt", 'r') as f:
    lines = [line.rstrip('\n') for line in f]

ranges = lines[0].split(",")

tups = [[int(tup) for tup in ranger.split("-")] for ranger in ranges]
strups = [ranger.split("-") for ranger in ranges]
lups = [[len(tup) for tup in ranger.split("-")] for ranger in ranges]
tot = 0
usefulRanges = []

def roundUp(tup1):
    tenPow = 10**(math.ceil(math.log10(tup1)) // 2)
    first1, second1 = tup1 // tenPow, tup1 % tenPow
    if first1 < second1:
        return (first1 + 1)*(tenPow + 1)
    else:
        return (first1)*(tenPow + 1)

def roundDown(tup2):
    tenPow = 10**(math.ceil(math.log10(tup1)) // 2)
    first2, second2 = tup2 // tenPow, tup2 % tenPow
    if first2 < second2:
        return (first2)*(tenPow + 1)
    else:
        return (first2 - 1)*(tenPow + 1)



for i in range(len(tups)):
    tup1, tup2 = tups[i][0], tups[i][1]
    lup1, lup2 = lups[i][0], lups[i][1]
    if lup1 == lup2 and lup1 % 2 == 0:
        usefulRanges += [[roundUp(tup1), roundDown(tup2)]]
    elif lup1 < lup2:
        upper = 10**(math.ceil(math.log10(tup1)))
        while upper < tup2:
            if len(str(tup1)) % 2 == 0:
                usefulRanges += [[roundUp(tup1), roundDown(upper)]]
            tup1 = upper + 1
            upper = min(10**(math.ceil(math.log10(tup1))), tup2)
        if len(str(tup1)) % 2 == 0:
            usefulRanges += [[roundUp(tup1), roundDown(tup2)]]

for tup1, tup2 in usefulRanges:
    diff = tup2 - tup1
    tenPow = 10**(math.ceil(math.log10(tup1)) // 2) + 1
    for i in range(tup1, tup2 + tenPow, tenPow):
        tot += i
print(tot)



"""
1. Find even lengths between lengths of numbers
2. for each even number length, find what things of form abcabc there are
3. sum them?
"""
