import pandas as pd
from numpy import genfromtxt
from matplotlib import pyplot as plt

a = [340, 1080, 640, 880, 990, 510]
b = [500, 1700, 800, 1100, 1400, 700]

r = (len(a))
sum1, sum2 = 0, 0

for i in range(0, r):
    sum1 = sum1 + float(a[i])
    sum2 = sum2 + float(b[i])

x1 = sum1 / r
y1 = sum2 / r
b1, b2, b3, b4, b5 = [], [], [], [], []
print(x1, y1)

# Calculate coefficients using the Ordinary Least Squares (OLS) method
# beta1 (Slope) = sum((x - mean_x)*(y - mean_y)) / sum((x - mean_x)^2)
s1, s2, sst = 0, 0, 0
for i in range(0, r):
    b1.append(float(a[i]) - x1)
    b2.append((float(b[i]) - y1))
    b3.append(float(b1[i]) * float(b2[i]))
    s1 = s1 + float(b3[i])
    b4.append((float(a[i]) - x1)**2)
    s2 = s2 + float(b4[i])

    b5.append((float(b[i]) - y1)**2)
    sst = sst + float(b5[i])

beta1 = s1 / s2

# beta0 (Intercept) = mean_y - beta1 * mean_x
beta0 = y1 - (beta1 * x1)
Y = beta0 + (beta1 * 790)
print("When rent is 790 ft then the area by regression is= ", Y)
print(beta0, beta1)

Y0, Y1, Y2 = [], [], []
ssr = 0
for i in range(0, r):
    Y0.append(beta0 + (beta1 * float(a[i])))
    Y1.append((float(Y0[i]) - y1)**2)
    ssr = ssr + (float(Y1[i]))

R = ssr / sst
print("The value of R squared= ", R)
po = []
li = []
t = ()

for i in range(len(a)):
    li.append(a[i])
    li.append(Y0[i])

    t = tuple(li)
    po.append(t)
    li.clear()

# Generate dataframe from list and write to xlsx
pd.DataFrame(po).to_excel('output.xlsx', header=False, index=False)

df = pd.read_excel('output.xlsx')
df.to_csv('output1.csv', index=False)
x, y = genfromtxt('output1.csv', unpack=True, delimiter=',')
plt.plot(x, y)
plt.plot(790, Y, 'o')
plt.plot(a, b, 'o')
plt.title('Linear Regression')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.grid()
plt.show()
