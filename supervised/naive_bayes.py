age = [30, 30, 35, 40, 40, 40, 35, 30, 30, 40, 30, 35, 35, 40]
# 30='<30', 35='31-40', 40='>40'
income = [20, 20, 20, 15, 10, 10, 10, 15, 10, 15, 15, 15, 20, 15]
# 20='high' 15='medium' 10='low'
student = [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0]
# 0=No, 1=Yes
credit = [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1]
# 0=fair, 1=Excellent
buy = [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0]
# 0=No, 1=Yes

# Enter new data set
newage = int(input("Enter the new Age: "))  # new input
newincome = int(input("Enter the new income: "))  # new input
newstudent = int(input("Enter the Student: "))  # new input
newcredit = int(input("Enter the new credit: "))  # new input

age_y = total_y = in_y = st_y = cr_y = buy_y = 0
age_n = total_n = in_n = st_n = cr_n = buy_n = 0
l = len(age)

# separate yes part and no part
for i in range(0, l):
    if buy[i] == 1:
        total_y += 1  # total number of yes
        if age[i] == newage:
            age_y += 1  # how many yes are there in case of that new data
        if income[i] == newincome:
            in_y += 1  # how many yes are there in case of that new data
        if student[i] == newstudent:
            st_y += 1  # how many yes are there in case of that new data
        if credit[i] == newcredit:
            cr_y += 1  # how many yes are there in case of that new data

    if buy[i] == 0:
        total_n += 1  # total number of no
        if age[i] == newage:
            age_n += 1  # how many no are there in case of that new data
        if income[i] == newincome:
            in_n += 1  # how many no are there in case of that new data
        if student[i] == newstudent:
            st_n += 1  # how many no are there in case of that new data
        if credit[i] == newcredit:
            cr_n += 1  # how many no are there in case of that new data

p_age_y = age_y / total_y  # probability of yes
p_age_n = age_n / total_n  # probability of no
p_income_y = in_y / total_y  # probability of yes
p_income_n = in_n / total_n  # probability of no
p_student_y = st_y / total_y  # probability of yes
p_student_n = st_n / total_n  # probability of no
p_credit_y = cr_y / total_y  # probability of yes
p_credit_n = cr_n / total_n  # probability of no

# Calculate Prior Probabilities: P(Class)
p_buy_y = total_y / (len(buy))  # probability of yes
p_buy_n = total_n / len(buy)  # probability of no

# Apply Naive Bayes Theorem: P(Y|X) ∝ P(X|Y) * P(Y)
# Assuming feature independence, total probability is the product of individual conditional probabilities
total_p_y = p_age_y * p_income_y * p_student_y * p_credit_y * p_buy_y  # total probability of yes
total_p_n = p_age_n * p_income_n * p_student_n * p_credit_n * p_buy_n  # total probability of no

# check which probability is greater and append the result
# Maximum A Posteriori (MAP) decision rule
if total_p_y > total_p_n:
    age.append(newage)
    income.append(newincome)
    student.append(newstudent)
    credit.append(newcredit)
    buy.append(1)
elif total_p_y < total_p_n:
    age.append(newage)
    income.append(newincome)
    student.append(newstudent)
    credit.append(newcredit)
    buy.append(0)

print(age)
print(income)
print(student)
print(credit)
print(buy)