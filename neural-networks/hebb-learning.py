# Hebb learning to print T and C
d = int(input("How many data set you want to insert: "))
t, c = [], []

for i in range(0, d):
    t.append(input("for T: "))

for i in range(0, d):
    c.append(input("For C: "))

b = 1
w = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y = [1, -1]
w1, w2 = [], []
t.append(int(b))
c.append(int(b))
temp, temp1 = [], []

# Apply the Hebbian Learning Rule: Weights are updated based on the product of input and target.
# "Neurons that fire together, wire together." Formula: delta_w = input * target
for i in range(0, d + 1):
    temp.append(int(t[i]) * (int(y[0])))

    w1.append((int(w[i]) + (int(temp[i]))))
    temp1.append(int(c[i]) * (int(y[1])))

for i in range(0, d + 1):
    w2.append(((int(w1[i])) + (int(temp1[i]))))

print(w1, w2)
n = len(t)
f1, f2 = [], []
c1 = 0
c2 = 0

for i in range(0, n - 1):
    f1.append(int(w2[i]) * int(t[i]))
    f2.append(int(w2[i]) * int(c[i]))
    c1 = c1 + int(f1[i])
    c2 = c2 + int(f2[i])

print(c1, c2)

if c1 >= 8:
    print("T")

if c2 <= -8:
    print("C")