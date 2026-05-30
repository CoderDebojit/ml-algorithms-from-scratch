from matplotlib import pyplot as plt

import random

d = int(input("Enter how many data set you want to insert: "))
a = []
print("Enter the data sets:")
for i in range(0, d):
    a.append(input())

c1 = random.choice(a)
c2 = random.choice(a)
c3 = random.choice(a)

if c1 == c2 or c1 == c3:
    c1 = random.choice(a)

if c2 == c1 or c2 == c3:
    c2 = random.choice(a)

if c3 == c1 or c3 == c1:
    c3 = random.choice(a)

print("The centroids are:", c1, c2, c3)

a.remove(c1)
a.remove(c2)
a.remove(c3)

l = len(a)
x, y, z = [], [], []

while True:
    x, y, z = [], [], []

    for i in range(0, l):
        val1 = ((float(c1) - float(a[i]))**2)
        val2 = ((float(c2) - float(a[i]))**2)
        val3 = ((float(c3) - float(a[i]))**2)
        mn = min(val1, val2, val3)
        if mn == val1:
            x.append(a[i])
        if mn == val2:
            y.append(a[i])
        if mn == val3:
            z.append(a[i])

    avg1 = 0
    for j in range(0, len(x)):
        avg1 = (avg1 + (float(x[j])))
    avg1 = avg1 / len(x)

    avg2 = 0
    for j in range(0, len(y)):
        avg2 = (avg2 + (float(y[j])))
    avg2 = avg2 / len(y)

    avg3 = 0
    for j in range(0, len(z)):
        avg3 = (avg3 + (float(z[j])))
    avg3 = avg3 / len(z)

    if avg1 == float(c1) and avg2 == float(c2) and avg3 == float(c3):
        break
    else:
        c1, c2, c3 = avg1, avg2, avg3

print(x, y, z)
plt.plot(x, 'o')
plt.plot(y, 'o')
plt.plot(z, 'o')
plt.ylabel("Numbers->")
plt.grid()
plt.show()