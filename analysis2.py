"""
This file contains one of the many analysis conducted under
the Unveristy Students Entrepreneurial Competency Research. 

The analysis question answerd in this file is :
    
    Are non STEM students more self-confident than STEM students
    and which one of them are more likely to become entrepreneurs? 

Conclusion in a Nutshell :  
    - non STEM students are as self-confident as STEM students
    - both STEM and non STEM students have the same competency 
      of being entrepreneur
"""

from data_preprocessing import data
import matplotlib.pyplot as plt 
import numpy as np

# -- a) Relation to self confidence
stem = data[data['is_stem'] == 1].groupby(['SelfConfidence']).count()['Age']
not_stem = data[data['is_stem'] == 0].groupby(['SelfConfidence']).count()['Age']

X = range(1, 6)
stem = [stem[index] for index in X]
stem = [(val * 100) / sum(stem) for val in stem]

not_stem = [not_stem[index] for index in X]
not_stem = [(val * 100) / sum(not_stem) for val in not_stem]

X_axis = np.arange(len(X))

plt.bar(X_axis - 0.2, stem, 0.4, label = 'STEM')
plt.bar(X_axis + 0.2, not_stem, 0.4, label = 'Non STEM')


  
plt.xticks(X_axis, X)
plt.xlabel("Lowest to Highest Confidence")
plt.ylabel("percentage of Students")

plt.legend()
plt.show()

# -- b) Relation to competency of being entrepreneur
stem = data[data['is_stem'] == 1].groupby(['y']).count()['Age']
not_stem = data[data['is_stem'] == 0].groupby(['y']).count()['Age']

X = range(2)
stem = [stem[index] for index in X]
stem = [(val * 100) / sum(stem) for val in stem]

not_stem = [not_stem[index] for index in X]
not_stem = [(val * 100) / sum(not_stem) for val in not_stem]

X_axis = np.arange(len(X))

plt.bar(X_axis - 0.2, stem, 0.4, label = 'STEM')
plt.bar(X_axis + 0.2, not_stem, 0.4, label = 'Non STEM')


  
plt.xticks(X_axis, ['incompetent', 'competent'])

plt.xlabel("competency of being entrepreneur")
plt.ylabel("percentage of Students")

plt.legend()
plt.show()