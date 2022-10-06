# Here is my simple solution to Leetcode 2: add two numbers!
#         https://leetcode.com/problems/add-two-numbers/
l1 = [2,34,5]
l2 = [4,5,6]


l11 = []
while len(l1) > 0:
    l11.append(str(l1[-1]))
    l1 = l1[:-1]
l1 = l11
l11 = []
while len(l2) > 0:
    l11.append(str(l2[-1]))
    l2 = l2[:-1]
l2 = l11
l1 = int("".join(l1))
l2 = int("".join(l2))
l11 = str(l1+l2)
l11 = list(l11)
l2 = []
while len(l11) > 0:
    l2.append(str(l11[-1]))
    l11 = l11[:-1]
l11 = l2
print(l11)