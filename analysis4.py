"""
This file contains one of the many analysis conducted under
the University Students Entrepreneurial Competency Research.

The analysis question answered in this file is:

    If a student is influenced, then what matters more: 
    confidence or projects? Is this different for STEM 
    and non STEM students?
    
Conclusion in a Nutshell:
- When a student is influenced, percentage of students undertaking projects and
having high self-confidence is similar.
- When a student is influenced, the percentage of STEM students and non-STEM students
with high self-confidence is similar.
- When a student is influenced, percentage of STEM students undertaking individual projects is slightly
higher than non-STEM students.

Note: High self-confidence is defined as a rating of 4 or 5 in self-confidence.
"""

from data_preprocessing import data
import matplotlib.pyplot as plt

# -- a) Relation of confidence and projects

# Extracting confidence of influenced students
very_influenced_confidence = data[data['Influenced'] == 1].groupby(['SelfConfidence']).count()['Age']

array_1 = [1, 2, 3, 4, 5]
array_2 = [very_influenced_confidence[x] for x in array_1]

high_conf = (array_2[3] + array_2[4]) * 100 / sum(array_2)

# Extracting projects of influenced students
very_influenced_projects = data[data['Influenced'] == 1].groupby(['IndividualProject']).count()['Age']

project_1 = [0, 1]
project_2 = [very_influenced_projects[x] for x in project_1]

ind_p = project_2[1] * 100 / sum(project_2)

lis_1 = [high_conf, ind_p]
lis_2 = ["High Self-Confidence", "Undertaken Project"]

fig = plt.figure(figsize=(10, 6))

# creating the bar plot
plt.bar(lis_2, lis_1, color='maroon',
        width=0.4)

plt.ylabel("Percentage of students")

plt.show()

# -- b) Relation of confidence for STEM and Non STEM students

# Extracting confidence for STEM students
very_influenced_confidence_stem = data[(data['Influenced'] == 1) & 
                                       (data["is_stem"] == 1)].groupby(['SelfConfidence']).count()['Age']

array_1 = [1, 2, 3, 4, 5]
array_2 = [very_influenced_confidence_stem[x] for x in array_1]

answer_confidence = (array_2[3] + array_2[4]) * 100 / sum(array_2)

# Extracting confidence for non-STEM students
very_influenced_confidence_non_stem = data[(data['Influenced'] == 1) &
                                           (data["is_stem"] == 0)].groupby(['SelfConfidence']).count()['Age']

array_2_non = [very_influenced_confidence_non_stem[x] for x in array_1]
answer_confidence_non = (array_2_non[3] + array_2_non[4]) * 100 / sum(array_2_non)

lis_1 = [answer_confidence, answer_confidence_non]
lis_2 = ["STEM", "Non-STEM"]

fig_3 = plt.figure(figsize=(10, 6))

# creating the bar plot
plt.bar(lis_2, lis_1, color='maroon',
        width=0.4)

plt.ylabel("Percentage of students with high self-confidence when influenced")
plt.xlabel("Degree type of students")

plt.show()

# -- c) Relation of individual projects for STEM and Non STEM students

# Extracting individual projects for STEM students
very_influenced_project_stem = data[(data['Influenced'] == 1) &
                                    (data["is_stem"] == 1)].groupby(['IndividualProject']).count()['Age']

array_1_p = [0, 1]
array_2_p = [very_influenced_project_stem[x] for x in array_1_p]

answer = array_2_p[1] * 100 / sum(array_2_p)

# Extracting individual projects for non-STEM students
very_influenced_projects_non_stem = data[(data['Influenced'] == 1) &
                                         (data["is_stem"] == 0)].groupby(['IndividualProject']).count()['Age']

array_2_non_p = [very_influenced_projects_non_stem[x] for x in array_1_p]
answer2 = array_2_non_p[1] * 100 / sum(array_2_non_p)

lis = [answer, answer2]
lis2 = ["STEM", "Non-STEM"]

fig_2 = plt.figure(figsize=(10, 6))

# creating the bar plot
plt.bar(lis2, lis, color='maroon',
        width=0.4)

plt.ylabel("Percentage of students undertaking individual projects when influenced")
plt.xlabel("Degree type of students")

plt.show()