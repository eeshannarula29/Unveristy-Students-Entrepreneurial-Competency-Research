"""
This file contains one of the many analysis conducted under
the University Students Entrepreneurial Competency Research.

The analysis question answered in this file is:

    What is the relation between having mental disorder
    and self-confidence or self-reliance? How does it
    change with age? Is it different for people who do
    not have a mental disorder?
    
Conclusion in a Nutshell :

With mental disorder:
    1. We find that more than half of the students with mental
       disorders have high self-confidence and self-reliance,
       and there is a slightly more percentage of these students
       having high self-reliance than high self-confidence.
    
    2. We see that there is no significant difference in the
       percentage of students having mental disorders and having
       high self-confidence from age 17 to 23. However, there is
       a spike in the percentage at age 25, and there are no 
       students who have a mental disorder and high self-confidence
       at age 24.
    
    3. We see that the percentage of students with mental disorders
       and having high self-reliance increases till age 20, after 
       which it again decreases.
    
Without mental disorder:
    1. We find that more than half of the students without mental 
       disorders have high self-confidence and self-reliance, and
       there is a significantly more percentage of these students 
       having high self-reliance than high self-confidence.
    
    2. We see that the percentage of students having mental disorders
       and having high self-confidence from age 18 to 22 decreases.
       However, there is a spike in the percentage at age 24, and there
       are no students who have a mental disorder and high self-confidence
       at age 23.
    
    3. We see that the percentage of students having mental disorders and
       having high self-reliance from age 17 to 21 gradually increases.
       However, there is a spike in the percentage at age 24, and there are
       no students who have a mental disorder and high self-reliance at age 23.
       There is also a significant decline in the percentage at age 22.
    
Note:
- High self-confidence is defined as a rating of 4 or 5 in self-confidence.
- High self-reliance is defined as a rating of 4 or 5 in self-reliance.
- In the analysis, zero percentages might be explained by the lack of data;
  however, the sudden spikes at ages 24 and 25 are worth further investigation. 
"""

from data_processing import data
import matplotlib.pyplot as plt

# a) Relation with self-confidence
mental_disorder_conf = data[data['MentalDisorder'] == 1].groupby(['SelfConfidence']).count()['Age']
array_1 = [1, 2, 3, 4, 5]
array_2 = [mental_disorder_conf[x] for x in array_1]
high_conf = (array_2[3] + array_2[4]) * 100 / sum(array_2)

# b) Relation with self-reliance
mental_disorder_rel = data[data['MentalDisorder'] == 1].groupby(['SelfReliance']).count()['Age']
array_3 = [mental_disorder_rel[x] for x in array_1]
high_rel = (array_3[3] + array_3[4]) * 100 / sum(array_3)

lis_1 = [high_conf, high_rel]
lis_2 = ["High Self-Confidence", "High Self-reliance"]

fig = plt.figure(figsize=(10, 6))

# creating the bar plot
plt.bar(lis_2, lis_1, color='maroon',
        width=0.4)

plt.ylabel("Percentage of students")
plt.show()

# c) Change with age
mental_disorder_age = data[data['MentalDisorder'] == 1]
mental_disorder_full = mental_disorder_age.groupby('Age').count()['Gender']
mental_disorder_age_c = mental_disorder_age[mental_disorder_age["SelfConfidence"] >= 4].groupby('Age').count()['Gender']
lis = [x for x in range(17, 24)]
lis.extend([25])
lis_2 = [mental_disorder_age_c[x] for x in lis]
lis_3 = [mental_disorder_full[x] for x in lis]
percentage = []
for x in range(len(lis_3)):
    percentage.append(lis_2[x] * 100 / lis_3[x])
res = {lis[i]: percentage[i] for i in range(len(percentage))}
plt.bar(res.keys(), res.values())
plt.xlabel("Age of students with mental disorders")
plt.ylabel("Percentage with high self-confidence")
plt.show()

mental_disorder_age_r = mental_disorder_age[mental_disorder_age["SelfReliance"] >= 4].groupby('Age').count()['Gender']
lis_r = [x for x in range(17, 23)]
lis_2_r = [mental_disorder_age_r[x] for x in lis_r]
lis_4 = [mental_disorder_full[x] for x in lis_r]
percentage_r = []
for x in range(len(lis_4)):
    percentage_r.append(lis_2_r[x] * 100 / lis_4[x])
res_r = {lis_r[i]: percentage_r[i] for i in range(len(percentage_r))}
plt.bar(res_r.keys(), res_r.values())
plt.xlabel("Age of students with mental disorders")
plt.ylabel("Percentage with high self-reliance")
plt.show()

# d) Relation with self-confidence -- No mental disorder
no_mental_disorder_conf = data[data['MentalDisorder'] == 0].groupby(['SelfConfidence']).count()['Age']
array_1 = [1, 2, 3, 4, 5]
array_2 = [no_mental_disorder_conf[x] for x in array_1]
high_conf_no = (array_2[3] + array_2[4]) * 100 / sum(array_2)

# e) Relation with self-reliance -- No mental disorder
no_mental_disorder_rel = data[data['MentalDisorder'] == 0].groupby(['SelfReliance']).count()['Age']
array_3 = [no_mental_disorder_rel[x] for x in array_1]
high_rel_no = (array_3[3] + array_3[4]) * 100 / sum(array_3)

lis_1 = [high_conf_no, high_rel_no]
lis_2 = ["High Self-Confidence", "High Self-reliance"]

fig = plt.figure(figsize=(10, 6))

# creating the bar plot
plt.bar(lis_2, lis_1, color='maroon',
        width=0.4)

plt.ylabel("Percentage of students")
plt.show()

# f) Change with age
no_mental_disorder_age = data[data['MentalDisorder'] == 0]
no_mental_disorder_full = no_mental_disorder_age.groupby('Age').count()['Gender']
no_mental_disorder_age_c = \
   no_mental_disorder_age[no_mental_disorder_age["SelfConfidence"] >= 4].groupby('Age').count()['Gender']

lis = [x for x in range(18, 23)]
lis.extend([24])
lis_2 = [no_mental_disorder_age_c[x] for x in lis]
lis_3 = [no_mental_disorder_full[x] for x in lis]
percentage = []
for x in range(len(lis_3)):
    percentage.append(lis_2[x] * 100 / lis_3[x])
res = {lis[i]: percentage[i] for i in range(len(percentage))}
plt.bar(res.keys(), res.values())
plt.xlabel("Age of students without mental disorders")
plt.ylabel("Percentage with high self-confidence")
plt.show()

no_mental_disorder_age_r = \
    no_mental_disorder_age[no_mental_disorder_age["SelfReliance"] >= 4].groupby('Age').count()['Gender']

lis_r = [x for x in range(17, 23)]
lis_r.extend([24])
lis_2_r = [no_mental_disorder_age_r[x] for x in lis_r]
lis_4 = [no_mental_disorder_full[x] for x in lis_r]
percentage_r = []
for x in range(len(lis_4)):
    percentage_r.append(lis_2_r[x] * 100 / lis_4[x])
res_r = {lis_r[i]: percentage_r[i] for i in range(len(percentage_r))}
plt.bar(res_r.keys(), res_r.values())
plt.xlabel("Age of students without mental disorders")
plt.ylabel("Percentage with high self-reliance")
plt.show()
