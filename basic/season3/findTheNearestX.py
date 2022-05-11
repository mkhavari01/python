x1 = 9
x2 = 16
x3 = 22


l = [x1-x2,x2-x1,x3-x2,x2-x3,x1-3]
filtered = list(filter(lambda item: item >= 0,l))
filtered.sort()
print(filtered)