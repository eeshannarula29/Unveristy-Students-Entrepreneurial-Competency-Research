# import libraraies
import pandas as pd

# load data
data = pd.read_csv('data.csv')

# remove unwanted columns
data = data.drop(columns=['ReasonsForLack'], axis=1)

# saving the unique values for lable encoding
values = {column: list(data[column].unique()) 
          for column in data.columns.values}

# Add a filed called no_of_degrees which is the number of degrees a student is pursuing.
# the 'EducationSector' column as degrees split by commas, so we would split the string value
# and count the length of that list. The length is the number of degrees. 
data['no_of_degrees'] = data['EducationSector'].apply(lambda val: len(val.split(',')))

# Add a filed called is_stem which tells whether a student has taken a science degree or not
stem_fields = ['Engineering Sciences',
               'Medicine, Health Sciences',
               'Mathematics or Natural Sciences'] 

data['is_stem'] = data['EducationSector'].apply(lambda val: 1 if val in stem_fields else 0)
    
# Lable encode the following columns: IndividualProject, Gender, City, Influenced, MentalDisorder
columns_to_lable = ['IndividualProject', 'Gender', 'City', 'Influenced', 'MentalDisorder']

for column in columns_to_lable:
    data[column] = data[column].apply(lambda val: values[column].index(val)) 

# Onehot encode the following columns : EducationSector, KeyTraits 
dummies_ed_sec = pd.get_dummies(data['EducationSector'], prefix='degree')
dummies_traits = pd.get_dummies(data['KeyTraits'], prefix='trait')

data = data.join(dummies_ed_sec.join(dummies_traits)).drop(columns=['EducationSector', 'KeyTraits'])       