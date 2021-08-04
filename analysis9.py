"""
This file contains one of the many analysis conducted under
the University Students Entrepreneurial Competency Research.

The analysis question answered in this file is:

    How does competitiveness change with age or degree?

Conclusion in a Nutshell:

- With age:
    We find that more that about 60% students have a high
    competitiveness at age 17. This percentage decreases
    for two years, and then increases at age 20, remaining
    almost the same for the upcoming ages. Then, there is a 
    spike in the percentage at age 24.

- With degree:
    We find that about 60% of STEM students have high competitiveness
    whereas 40% of non-STEM students have high competitiveness.

Note:
    High competitiveness is defined as a rating of 4 or 5 on
    competitiveness.
"""

from data_preprocessing import data
import matplotlib.pyplot as plt

# a) Change with age
change_with_age = data[data['Competitiveness'] >= 4].groupby('Age').count()['Gender']

lis = [x for x in range(17, 25)]
full_age = data.groupby('Age').count()['Gender']

lis_2 = [change_with_age[x] for x in lis]
lis_3 = [full_age[x] for x in lis]
percentage = []
for x in range(len(lis_3)):
    percentage.append(lis_2[x] * 100 / lis_3[x])
res = {lis[i]: percentage[i] for i in range(len(percentage))}
plt.bar(res.keys(), res.values())
plt.xlabel("Age of students")
plt.ylabel("Percentage with high competitiveness")
plt.show()

# b) Change with degree
change_with_degree = data[data['Competitiveness'] >= 4].groupby('is_stem').count()['Gender']

lis = [0, 1]
full_degree = data.groupby('is_stem').count()['Gender']

lis_2 = [change_with_degree[x] for x in lis]
lis_3 = [full_degree[x] for x in lis]
percentage = []
for x in range(len(lis_3)):
    percentage.append(lis_2[x] * 100 / lis_3[x])
res = {lis[i]: percentage[i] for i in range(len(percentage))}
lis_2 = ["Non-STEM Degree", "STEM Degree"]

fig = plt.figure(figsize=(10, 6))

# creating the bar plot
plt.bar(lis_2, percentage, color='maroon',
        width=0.4)

plt.ylabel("Percentage of students")
plt.show()
