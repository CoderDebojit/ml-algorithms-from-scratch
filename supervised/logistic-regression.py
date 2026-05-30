import math

c = c1 = k = f = 0
x1, y1, x2, y = [], [], [], []

n = int(input("Enter the data you want to insert: "))

for i in range(0, n):
    x1.append(input("Enter the x1 data set: "))

for i in range(0, n):
    x2.append(input("Enter the x2 data set: "))

for i in range(0, n):
    y.append(input("Enter the y data set: "))

b0 = b1 = b2 = 0
alpha = 0.1

while True:
    for i in range(0, n):
        # Calculate linear combination
        k = b0 + b1 * (float(x1[i])) + b2 * (float(x2[i]))

        # Apply Sigmoid activation to map to a probability between 0 and 1
        pre = (1 / (1 + (math.e)**(-k)))

        # Update weights using Gradient Ascent to maximize Log-Likelihood
        b0 = b0 + alpha * (float(y[i]) - pre) * pre * (1 - pre) * 1.0
        b1 = b1 + alpha * (float(y[i]) - pre) * pre * (1 - pre) * (float(x1[i]))
        b2 = b2 + alpha * (float(y[i]) - pre) * pre * (1 - pre) * (float(x2[i]))
        k1 = b0 + b1 * (float(x1[i])) + b2 * (float(x2[i]))
        pre1 = (1 / (1 + (math.e)**(-k1)))

        f = f + 1

        if pre1 > 0.5:
            y1.append(1)
        elif pre1 < 0.5:
            y1.append(0)

    for i in range(0, n):
        if float(y[i]) == float(y1[i]):
            c = c + 1
        else:
            c1 = c1 + 1

    if f == n:
        break

acc = (c / n) * 100
print("True Positive classifications is", c)
print("False Positive Classifications is", c1)
print("Hence the Accuracy is", acc)
