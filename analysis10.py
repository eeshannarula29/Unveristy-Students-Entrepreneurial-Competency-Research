"""
This file contains one of the many analysis conducted under
the University Students Entrepreneurial Competency Research.
The analysis question answered in this file is:
Is there a relation between not having mental disorders and being influenced by someone?

Conclusion:
There is no significant difference in the percentage of students with or without mental disorders
who are influenced by someone.
"""

from data_processing import data
import matplotlib.pyplot as plt

no_mental_disorder = data[data['MentalDisorder'] == 0].groupby("Influenced").count()['Age']
lis = [0, 1]
lis_2 = [no_mental_disorder[x] for x in lis]
influenced = lis_2[1] / sum(lis_2)

mental_disorder = data[data['MentalDisorder'] == 1].groupby("Influenced").count()['Age']
print(mental_disorder)
lis_3 = [mental_disorder[x] for x in lis]
influenced_1 = lis_3[1] / sum(lis_3)

plot = [influenced, influenced_1]
plot_1 = ["No mental disorder", "Mental disorder"]
fig = plt.figure(figsize=(10, 6))

# creating the bar plot
plt.bar(plot_1, plot, color='maroon',
        width=0.4)

plt.ylabel("Percentage of students influenced")
plt.show()
