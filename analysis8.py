"""
This file contains one of the many analysis conducted under
the University Students Entrepreneurial Competency Research.

The analysis question answered in this file is:
What is the correlation between a strong need to achieve something or the desire to
take initiative and the probability of becoming an entrepreneur?

Conclusion:
1.
We see that 60% of students with no probability of becoming an entrepreneur had a high need to achieve
something, and 70% of students with probability of becoming an entrepreneur had a high need to achieve
something.
2.
We see that 55% of students with no probability of becoming an entrepreneur had a high desire to take
initiative, and 70% of students with probability of becoming an entrepreneur had a high desire to take
initiative.

Note:
High desire to take initiative and high need to achieve something is defined as a rating of 4 or 5 on
their respective scales.
"""
from data_processing import data
import matplotlib.pyplot as plt

# a) Strong need to achieve something
strong_need = data[data['StrongNeedToAchieve'] >= 4].groupby('y').count()['Gender']

lis = [0, 1]
full_need = data.groupby('y').count()['Gender']

lis_2 = [strong_need[x] for x in lis]
lis_3 = [full_need[x] for x in lis]
percentage = []
lis_4 = ["0", "1"]
for x in range(len(lis_3)):
    percentage.append(lis_2[x] * 100 / lis_3[x])
fig = plt.figure(figsize=(10, 6))

# creating the bar plot
plt.bar(lis_4, percentage, color='maroon',
        width=0.4)
plt.ylabel("Percentage of students with high need to achieve something")
plt.xlabel("Probability of becoming an entrepreneur")
plt.show()

# b) Desire to take initiative
strong_desire = data[data['DesireToTakeInitiative'] >= 4].groupby('y').count()['Gender']

lis = [0, 1]
full_desire = data.groupby('y').count()['Gender']

lis_2 = [strong_desire[x] for x in lis]
lis_3 = [full_desire[x] for x in lis]
percentage = []
lis_4 = ["0", "1"]
for x in range(len(lis_3)):
    percentage.append(lis_2[x] * 100 / lis_3[x])
fig = plt.figure(figsize=(10, 6))

# creating the bar plot
plt.bar(lis_4, percentage, color='maroon',
        width=0.4)
plt.ylabel("Percentage of students with high desire to take initiative")
plt.xlabel("Probability of becoming an entrepreneur")
plt.show()
