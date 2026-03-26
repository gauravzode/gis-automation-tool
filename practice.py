a = [1, 2, 3, 4, 5, 6, 7]
c = []

largest = a[0]

for i in a:
    if i > largest:
        largest = i
print (largest)


for i in a:
    if i < largest:
        c.append(i)
print (c)


for i in c:
    if i > c[0]:
        largest = i
print (largest)
        
