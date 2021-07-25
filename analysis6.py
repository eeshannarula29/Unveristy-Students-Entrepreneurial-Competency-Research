"""
This file contains one of the many analysis conducted under
the Unveristy Students Entrepreneurial Competency Research. 

The analysis question answerd in this file is : 

    Is there a difference in the mental and physical health of people
    who may or may not become entrepreneurs?   

Conclusion in a Nutshell : No, it is not, atleast not in our dataset.   
"""

from data_preprocessing import data
import matplotlib.pyplot as plt 

# -- a) Assosiation with Mental health
fig, ax = plt.subplots()
fig.set_size_inches(15.5, 7.5)

counts = data[data['y'] == 1].groupby(['MentalDisorder']).count()['y']
another_counts = data[data['y'] == 0].groupby(['MentalDisorder']).count()['y']

ax.bar(['mental disorder - entrepreneur',
        'no mental disorder - entrepreneur',
        'mental disorder - not entrepreneurs',
        'no mental disorder - not entrepreneur'],
       [counts[0], counts[1], another_counts[0], another_counts[1]])

ratio_1_calc = round(counts[0] / (counts[0] + another_counts[0]) * 1000) / 10
ratio_2_calc = round(counts[1] / (counts[1] + another_counts[1]) * 1000) / 10

ratio_1 = f'percentage of people with metal health disorder who have the potential to become entrepreneur : {ratio_1_calc}%'
ratio_2 = f'percentage of people who are mentaly fit and have the potential to become entrepreneur : {ratio_2_calc}%'

ax.set_xlabel('has mental disorder or not \n' + ratio_1 + '\n' + ratio_2)
ax.set_ylabel('number of students who might become entreprenures')

ax.set_title('Mental health vs no of students who can become entreprenures')

plt.show()

# -- b) Assosiation with Physical health
fig, ax = plt.subplots()
fig.set_size_inches(15.5, 7.5)

counts = data[data['y'] == 1].groupby(['GoodPhysicalHealth']).count()['y']
another_counts = data[data['y'] == 0].groupby(['GoodPhysicalHealth']).count()['y']

ax.bar(['bad physical health - entrepreneur',
        'good physical health - entrepreneur',
        'bad physical health- not entrepreneur',
        'good physical health - not entrepreneur'],
       [counts[1] + counts[2] + counts[3], counts[4] + counts[5],
        another_counts[1] + another_counts[2] + another_counts[3],
        another_counts[4] + another_counts[5]])

ratio_1_calc = round((counts[1] + counts[2] + counts[3]) /
                     ((counts[1] + counts[2] + counts[3]) +
                      (another_counts[1] + another_counts[2] + another_counts[3])) * 1000) / 10

ratio_2_calc = round((counts[4] + counts[5]) /
                     ((counts[4] + counts[5]) + (another_counts[4] +  another_counts[5])) * 1000) / 10

ratio_1 = f'percentage of people with bad physical health who have the potential to become entrepreneur : {ratio_1_calc}%'
ratio_2 = f'percentage of people who are physically fit and have the potential to become entrepreneur : {ratio_2_calc}%'

ax.set_xlabel('rating from worst to best physical health \n' + ratio_1 + '\n' + ratio_2)
ax.set_ylabel('number of students who might become entreprenures')

ax.set_title('Physical health vs no of students who can become entreprenures')

plt.show()