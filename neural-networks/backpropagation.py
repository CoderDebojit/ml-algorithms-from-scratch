import pandas as pd
import math
import random

df = pd.read_csv("Sample_Dataset_BACKPROP.csv")  # sample data set

# Read columns
x1 = df['X1']
x2 = df['X2']
y = df['Y']
f = 0
epoch = int(input("Epoch: "))  # How many times it iterates

# set random weights and bias
w11, w12, w21, w22, wh1, wh2 = random.uniform(0.1, 0.9), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9)
b1, b2 = random.uniform(0.1, 0.9), random.uniform(0.1, 0.9)

# h1_in, h1_out, h2_in, h2_out, o1_in, o2_in, o1_p_out, o2_p_out = [], [], [], [], [], [], [], []
a = 0.1  # learning rate

while True:
    for i in range(0, len(x1)):

        # net input for hidden layer
        h1_in = w11 * x1[i] + w21 * x2[i] + b1 * 1
        h2_in = w12 * x1[i] + w22 * x2[i] + b1 * 1

        # net output for hidden layer
        h1_out = 1 / (1 + (math.e**(-h1_in)))
        h2_out = 1 / (1 + (math.e**(-h2_in)))

        # net input for output layer
        o1_in = wh1 * h1_out + wh2 * h2_out + b2 * 1

        # net output for output layer
        o1_out = 1 / (1 + (math.e**(-(o1_in))))

        # Calculate Mean Squared Error (MSE) component
        error = (o1_out - y[i])**2

        # Update the weights using backpropagation
        # Formula: w_new = w_old - learning_rate * (derivative of error with respect to weight)
        w11 = w11 - (a * (((o1_out - y[i]) * (o1_out * (1 - o1_out)) * wh1)) * (h1_out * (1 - h1_out)) * x1[i])
        w21 = w21 - (a * (((o1_out - y[i]) * (o1_out * (1 - o1_out)) * wh1)) * (h1_out * (1 - h1_out)) * x2[i])
        w12 = w12 - (a * (((o1_out - y[i]) * (o1_out * (1 - o1_out)) * wh2)) * (h2_out * (1 - h2_out)) * x1[i])
        w22 = w22 - (a * (((o1_out - y[i]) * (o1_out * (1 - o1_out)) * wh2)) * (h2_out * (1 - h2_out)) * x2[i])

        wh1 = wh1 - (a * ((o1_out - y[i]) * (o1_out * (1 - o1_out)) * h1_out))
        wh2 = wh2 - (a * ((o1_out - y[i]) * (o1_out * (1 - o1_out)) * h2_out))

    f += 1
    if error <= 0.001:  # minimize error to a certain value
        break
    if f == epoch:  # epoch and iteration are equal then
        break

print("The error is=", error, "after", f, "epoch")  # print output