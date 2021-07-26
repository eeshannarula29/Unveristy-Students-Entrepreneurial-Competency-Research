"""
This file contains one of the many analysis conducted under
the Unveristy Students Entrepreneurial Competency Research. 

The analysis question answerd in this file is : 

    Does pursuing more than one degree/program affect the number of
    projects, desire to take initiative, and finally the probability
    of being an entrepreneur change? 
    
Conclusion in a Nutshell :
    - there is no significant change in the Individual Project
    - desire to take initiative decreases a bit for people who 
      take more than one degree
    - competency of being entrepreneur is less for people who 
      take more than one degree 
"""
    
from data_preprocessing import data
import matplotlib.pyplot as plt 


# -- a) Relation with number of projects
more_than_one_degree = data[data['no_of_degrees'] > 1].groupby(['IndividualProject']).count()['Age']
only_one_degree = data[data['no_of_degrees'] <= 1].groupby(['IndividualProject']).count()['Age']

percentage1 = only_one_degree[1] / (only_one_degree[1] + only_one_degree[0]) * 100
percentage2 = more_than_one_degree[1] / (more_than_one_degree[1] + more_than_one_degree[0]) * 100

fig, ax = plt.subplots()

ax.bar(['one degree', 'more than one degree'], [percentage1 ,percentage2])

ax.set_xlabel('number of degrees')
ax.set_ylabel('percentage of student who made a project')

ax.set_title('Number of degrees vs student made a project')

plt.show()

# -- b) Relation to desire to take intiative
more_than_one_degree = data[data['no_of_degrees'] > 1].groupby(['DesireToTakeInitiative']).count()['Age']
only_one_degree = data[data['no_of_degrees'] <= 1].groupby(['DesireToTakeInitiative']).count()['Age']

fig = plt.figure()

ax1 = fig.add_axes([0, 0, .5, .5], aspect=1)
values = [only_one_degree[index + 1] for index in range(5)]
ax1.pie(values, labels=['1', '2', '3', '4', '5'], startangle=90, shadow=True,explode=(0.1, 0.1, 0.1, 0.1, 0.1), autopct='%1.2f%%')
ax1.set_title('one degree')

ax2 = fig.add_axes([.5, .0, .5, .5], aspect=1)
values = [more_than_one_degree[index + 1] for index in range(5)]
ax2.pie(values, labels=['1', '2', '3', '4', '5'], startangle=90, shadow=True,explode=(0.1, 0.1, 0.1, 0.1, 0.1), autopct='%1.2f%%')
ax2.set_title('more than one degree')

plt.show()

# -- c) Relation to competency of being entrepreneur
more_than_one_degree = data[data['no_of_degrees'] > 1].groupby(['y']).count()['Age']
only_one_degree = data[data['no_of_degrees'] <= 1].groupby(['y']).count()['Age']

percentage1 = only_one_degree[1] / (only_one_degree[1] + only_one_degree[0]) * 100
percentage2 = more_than_one_degree[1] / (more_than_one_degree[1] + more_than_one_degree[0]) * 100

fig, ax = plt.subplots()

ax.bar(['one degree', 'more than one degree'], [percentage1 ,percentage2])

ax.set_xlabel('number of degrees')
ax.set_ylabel('percentage of student who are compitent to become entrepreneur')

ax.set_title('Number of degrees vs student compitent to become entrepreneur')

plt.show()