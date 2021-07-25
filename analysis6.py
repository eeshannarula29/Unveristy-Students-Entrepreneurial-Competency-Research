"""
This file contains one of the many analysis conducted under
the Unveristy Students Entrepreneurial Competency Research. 

The analysis question answerd in this file is : 

    Is there a difference in the mental and physical health of people
    who may or may not become entrepreneurs?    
"""

from data_preprocessing import data
import matplotlib.pyplot as plt 

# -- a) Assosiation with Mental health
fig, ax = plt.subplots()

counts = data[data['y'] == 1].groupby(['MentalDisorder']).count()['y']

ax.bar(['mental disorder', 'no mental disorder'], [counts[0], counts[1]])

# plt.xlabel = 'has mental disorder or not'
# plt.ylabel = 'number of students who might become entreprenures'

ax.set_xlabel('has mental disorder or not')
ax.set_ylabel('number of students who might become entreprenures')

ax.set_title('Mental health vs no of students who can become entreprenures')

plt.show()

# -- b) Assosiation with Physical health
fig, ax = plt.subplots()

counts = data.groupby(['GoodPhysicalHealth']).count()['y']

ax.bar(['1', '2', '3', '4', '5'], [counts[1], counts[2], counts[3], counts[4], counts[5]])

ax.set_xlabel('rating from worst to best physical health')
ax.set_ylabel('number of students who might become entreprenures')

ax.set_title('Physical health vs no of students who can become entreprenures')

plt.show()