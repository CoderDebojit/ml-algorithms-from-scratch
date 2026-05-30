import math

outlook = [20, 20, 20, 20, 15, 15, 15, 15, 15, 10, 10, 10, 10, 10]
temp_num = [83, 64, 72, 81, 70, 68, 65, 75, 71, 85, 80, 72, 69, 75]
temp_nom = [15, 5, 10, 15, 10, 5, 5, 10, 10, 15, 15, 10, 5, 10]
hum_num = [86, 65, 90, 75, 96, 80, 70, 80, 91, 85, 90, 95, 70, 70]
hum_nom = [2, -2, 2, -2, 2, -2, -2, -2, 2, 2, 2, 2, -2, -2]
windy = [-1, 1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, 1]
pay = [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1]

newdata_outlook = int(input("Enter the new data for outlook data set: "))
newdata_temp_num = int(input("Enter the new data for temp_num data set: "))
newdata_temp_nom = int(input("Enter the new data for temp_nom data set: "))
newdata_hum_num = int(input("Enter the new data for hum_num data set: "))
newdata_hum_nom = int(input("Enter the new data for hum_nom data set: "))
newdata_windy = int(input("Enter the new data for windy data set: "))

# How many data you want to compare
k = int(input("Enter how many nearest data set you want to compare: "))

# n1=[15,80,5,66,-2,-1]
n = len(outlook)
p1, p2, p3, p4 = [], [], [], []

# Find out the Euclidean distance
# Calculate Euclidean Distance across all 6 features
# Formula: sqrt( Σ(x_i - y_i)^2 )
for i in range(0, n):
    p1.append(math.sqrt((outlook[i] - newdata_outlook)**2 + (temp_num[i] - newdata_temp_num)**2 + ((temp_nom[i] - newdata_temp_nom)**2) + ((hum_num[i] - newdata_hum_num)**2) + ((hum_nom[i] - newdata_hum_nom)**2) + ((windy[i] - newdata_windy)**2)))
    # store Euclidean distance value to another list
    p2.append(p1[i])

# Sort the new list, other remain same
p2.sort()

while True:
    # Check k value is odd or even
    if k % 2 == 0:
        # Even case
        print("Select the odd data set:")
        k = int(input("Enter how many nearest data set you want to consider: "))
        break
    else:
        # odd case (It is preferable)
        break

for j in range(0, k):
    # store sorted list value up to k range where k you given
    p3.append(p2[j])

for i in range(0, k):
    for j in range(0, n):
        # now check where the new values are present in the initial data set and store them to a list
        if p3[i] == p1[j]:
            p4.append(j)

# sort new list to maintain the numbering
p4.sort()

# length of the new list
l = len(p4)

# two counter variables
c1, c2 = 0, 0
for i in range(0, l):
    # check class value is true or not
    if pay[p4[i]] == 1:
        c1 += 1
    elif pay[p4[i]] == 0:
        c2 += 1

if c1 > c2:
    outlook.append(newdata_outlook)
    temp_num.append(newdata_temp_num)
    temp_nom.append(newdata_temp_num)
    hum_num.append(newdata_hum_num)
    hum_nom.append(newdata_hum_nom)
    windy.append(newdata_windy)
    pay.append(1)
elif c1 < c2:
    outlook.append(newdata_outlook)
    temp_num.append(newdata_temp_num)
    temp_nom.append(newdata_temp_nom)
    hum_num.append(newdata_hum_num)
    hum_nom.append(newdata_hum_nom)
    windy.append(newdata_windy)
    pay.append(0)

# print result
print(outlook)
print(temp_num)
print(temp_nom)
print(hum_num)
print(hum_nom)
print(windy)
print(pay)
print('values:', p4)