# coding:utf8

def calculate(l):
    if len(l) <= 1:
        return l[0]
    value = calculate(l[1: ])
    return 10 ** (len(l)-1) * l[0] + value

l1 = [1, 2, 3, 4, 5]
l2 = [4, 5]
sum = 0

result = calculate(l1)+calculate(l2)
print result