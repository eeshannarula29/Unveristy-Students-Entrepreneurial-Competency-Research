"""
This file contains one of the many analysis conducted under
the Unveristy Students Entrepreneurial Competency Research. 

The analysis question answerd in this file is : 

    Which traits are most and least helpful for being an
    entrepreneur and do these traits differ for people 
    from and not from a city?

Conclusion in a Nutshell : 
    - The order is Positivity > Passion > Work ethic > Vision > Resiliance
    - The order is same for both city and remote areas.
"""

from data_preprocessing import data
import matplotlib.pyplot as plt 
import numpy as np

traits = ['trait_Passion',
          'trait_Positivity',
          'trait_Resilience',
          'trait_Vision',
          'trait_Work Ethic']

def get_vals(d, is_remote = False):
    """Return no of entrepreneurs corresponding to traits"""
    if not is_remote:
        return [d[1][0][0][0][0],
                d[0][1][0][0][0],
                d[0][0][1][0][0],
                d[0][0][0][1][0],
                d[0][0][0][0][1]] 
        
    return [d[1][0][0][0][0],
            d[0][1][0][0][0],
            0,
            d[0][0][0][1][0],
            0]     
                

def get_percent_vals(d, is_remote = False):
    """Return percentage of entrepreneurs corresponding to traits"""
    vals = get_vals(d, is_remote)
    return [(val * 100) / sum(vals) for val in vals]
    
# -- a) Simple relation in traits and competency of being entrepreneur
ploting_data = data[data['y'] == 1].groupby(traits).count()['Age']

plt.bar(traits, get_vals(ploting_data))

plt.xlabel("trait")
plt.ylabel("Number of Students who have the competency of being entrepreneur")

plt.show()

# -- b) Difference in City and Remote
query_city = 'y == 1 and City == 0'
query_remote = 'y == 1 and City == 1'

city = data.query(query_city).groupby(traits).count()['Age']
remote = data.query(query_remote).groupby(traits).count()['Age']

X_axis = np.arange(len(traits))

city_y = get_percent_vals(city, False)
remote_y = get_percent_vals(remote, True)


plt.bar(X_axis - 0.2, city_y, 0.4, label = 'City')
plt.bar(X_axis + 0.2, remote_y, 0.4, label = 'Remote')

plt.xticks(X_axis, traits)

plt.xlabel("trait")
plt.ylabel("Number of Students who have the competency of being entrepreneur")

plt.legend()
plt.show()

