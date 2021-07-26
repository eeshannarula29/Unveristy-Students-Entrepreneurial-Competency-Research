"""
This file contains one of the many analysis conducted under
the Unveristy Students Entrepreneurial Competency Research. 

The analysis question answerd in this file is :
    
    Does competitiveness affect the 
    physical health and mental disorder condition of a student? 

Conclusion in a Nutshell :  
    - as the competitiveness increase the number of students
      with mental disorder increase
    - as the competitiveness increase the number of students
      with good physical health increase
"""

from data_preprocessing import data
import matplotlib.pyplot as plt 

# -- a) Relation to Mental Disorder Condition
vals = data[data['MentalDisorder'] == 1].groupby(['Competitiveness']).count()['Age']

X = range(1, 6)
y = [vals[index] for index in X]

fig, ax = plt.subplots()

ax.plot(X, y, '--')
ax.scatter(X, y, marker='P', color='red')

ax.set_xlabel('competitiveness')
ax.set_ylabel('number of students with mental disorder')

plt.show()

# -- b) Relation to Physical health
vals = data[data['GoodPhysicalHealth'] >= 3].groupby(['Competitiveness']).count()['Age']

X = range(1, 6)
y = [vals[index] for index in X]

fig, ax = plt.subplots()

ax.plot(X, y, '--')
ax.scatter(X, y, marker='P', color='red')

ax.set_xlabel('competitiveness')
ax.set_ylabel('number of students with good physical health')

plt.show()