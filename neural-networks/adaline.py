x1 = [1, -1, 1, 1]
x2 = [1, 1, 1, -1]
x3 = [1, -1, 1, -1]
x4 = [1, -1, -1, 1]
t = [1, 1, -1, -1]

w0, w1, w2, w3, w4 = 0, 0.1, 0.2, 0.4, 0.5
deltaw1, deltaw2, deltaw3, deltaw4 = [], [], [], []
alpha = 0.3
bias = 0.2
y, yout, error = [], [], []
l = len(x1)
weight1, weight2, weight3, weight4 = [], [], [], []
epoc = int(input("Enter how many epochs you want: "))
f = 0

while True:
    for i in range(0, l):
        y.append(bias * w0 + w1 * x1[i] + w2 * x2[i] + w3 * x3[i] + w4 * x4[i])
        error.append(t[i] - y[i])

        # Update the weights
        # Apply the ADALINE LMS (Least Mean Squares) Delta Rule for weight updates
        # Formula: w(new) = w(old) + alpha * (target - output) * input
        w0 = w0 + alpha * (t[i] - y[i])
        w1 = w1 + alpha * (t[i] - y[i]) * x1[i]
        w2 = w2 + alpha * (t[i] - y[i]) * x2[i]
        w3 = w3 + alpha * (t[i] - y[i]) * x3[i]
        w4 = w4 + alpha * (t[i] - y[i]) * x4[i]
        # bias = bias + alpha * (t[i] - (y[i]))
        weight1.append(w1)
        weight2.append(w2)
        weight3.append(w3)
        weight4.append(w4)
        deltaw1.append(alpha * (t[i] - (y[i])) * x1[i])
        deltaw2.append(alpha * (t[i] - (y[i])) * x2[i])
        deltaw3.append(alpha * (t[i] - (y[i])) * x3[i])
        deltaw4.append(alpha * (t[i] - (y[i])) * x4[i])

        if y[i] > 0:
            yout.append(1)
        elif y[i] <= 0:
            yout.append(-1)

    f = f + 1

    if f == epoc:
        break

print("After completing ", epoc, " epochs:")
print("So the y-input data values are:")
print(y)
print("The errors are:")
print(error)
print("The Delta w1, w2, w3, w4 is=")
print(deltaw1)
print(deltaw2)
print(deltaw3)
print(deltaw4)
print("The weights are:")
print(weight1)
print(weight2)
print(weight3)
print(weight4)
print("Applying the activation function then:")
print("The output is:")
print(yout)