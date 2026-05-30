# k-medoid
x = [2, 3, 3, 4, 6, 6, 7, 7, 8, 7]  # given data set
y = [6, 4, 8, 7, 2, 4, 3, 4, 5, 6]  # given data set

l = len(x)
c_p_1, c_p_2 = 0, 1  # position

c1, c2 = [], []  # save cluster values separately

distance_c1, distance_c2, cost_min, total_cost_val = [], [], [], []

while True:
    centroid1 = [x[c_p_1], y[c_p_1]]  # centroid-1 cluster values
    centroid2 = [x[c_p_2], y[c_p_2]]  # centroid-2 cluster values

    # Calculate Manhattan distance (|x1 - x2| + |y1 - y2|) for robust clustering around medoids
    for i in range(0, l):
        distance_c1.append(abs(x[i] - centroid1[0]) + abs(y[i] - centroid1[1]))  # All distance for centroid-1
        distance_c2.append(abs(x[i] - centroid2[0]) + abs(y[i] - centroid2[1]))  # All distance for centroid-2

        min_value = min(distance_c1[i], distance_c2[i])  # check which distance value is minimum

        cost_min.append(min_value)  # store all the minimum distance values in a list

    sum_cost = sum(cost_min)  # sum all minimum distances
    total_cost_val.append(sum_cost)  # store it to a list
    c_p_2 += 1  # centroid-2 position

    if c_p_2 == l:  # while loop continue until centroid-2 reaches the last position
        break
    else:
        distance_c1.clear()
        distance_c2.clear()
        cost_min.clear()

min_cost = min(total_cost_val)  # check which total cost is minimum

for i in range(0, (len(total_cost_val))):
    if min_cost == total_cost_val[i]:
        centroid1 = [x[0], y[0]]  # centroid-1 remains same
        centroid2 = [x[i + 1], y[i + 1]]  # centroid position where the total cost is minimum
        for j in range(0, l):
            distance_c1.append(abs(x[j] - centroid1[0]) + abs(y[j] - centroid1[1]))  # All distance for centroid-1
            distance_c2.append(abs(x[j] - centroid2[0]) + abs(y[j] - centroid2[1]))  # All distance for centroid-2

            min_value = min(distance_c1[j], distance_c2[j])  # check which distance value is minimum

            cost_min.append(min_value)
            # now cluster is built
            if min_value == distance_c1[j]:
                c1.append((x[j], y[j]))
            elif min_value == distance_c2[j]:
                c2.append((x[j], y[j]))

print("The all costs are:")
print(total_cost_val)
print("centroid1 is=", centroid1, "centroid2 is=", centroid2)
print("Best clustering is:")
print("cluster-1=", c1)
print("cluster-2=", c2)