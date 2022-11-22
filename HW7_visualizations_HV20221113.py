# Homework 7 Visualizations 
# Create 4 visualizations using the breast cancer dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
newline = '\n'

data = pd.read_csv('breast-cancer.csv')
#print(newline, data.head       # There are no headers in the dataframe

### The data does not have headers so read in txt file
 ## Use enumerate to assign a number to each line, strip white space, prints a list of tuples
 ## select the lines from the list that have the column attributes, print to find out which ones they are
 ## only select the second item in tuple for each item
with open('breast-cancer.txt') as f:
    lines = [(i, line.strip()) for i, line in enumerate(f.readlines())]
    attributes = [x[1] for x in lines[52:62]]

# To print out the attribute names and definitions
print(f'{newline}The attributes for each column are:')
[print(x) for x in attributes] 

# string split the attributes first by colon then by white space to get column names
colnames = [x.split()[1] for x in (i.split(':')[0] for i in attributes)]
print(newline, 'Column names: ', colnames)

# add columns to data and print new dataframe with column headers
data.columns = colnames
print(newline, data.head())


### Visualization 1 ------------------------------------------------------------------
## Get the data in proportions for each category
## get counts for each category and divide by total 
## Add the result for each column as a dictionary to a list (i.e. list of dicts) 
prop = []
for col in data:
    x = data[col].value_counts()/len(data)
    prop.append(dict(x))
print(prop[0])

## This graph is to get a general idea for how frequent each feature is for each column
## Stacked bar graph. Each column is stacked by the proportion of each category. So the total for each column is one.
pd.DataFrame(prop).plot(kind = 'bar', stacked = True, cmap = 'turbo', width = 1).set_aspect(8)
plt.xticks(range(10), data.columns)
plt.title('Proportion of Breast Cancer Patients with Attribute')
plt.xlabel("Phenotype")
plt.ylabel("Proportion of dataset")

plt.legend(loc = 'upper right', bbox_to_anchor = (1.25, 1), fontsize = 'small', labelspacing = .05)
plt.show()

### Visualization 2 -----------------------------------------------------------------------------------
## group by recurrent or not and calculate the proportion per tumor size group
## reset index to turn back into dataframe format
## pivot on the recurrent/not recurrent with each tumor size group as row and counts as values
## convert the counts to proportion of the total recurrent or not recurrent events
data_by_class = data.groupby('Class')['tumor-size'].value_counts().to_frame('counts')
data_by_class.reset_index(inplace = True)
data_by_class = pd.DataFrame(data_by_class).pivot(index = 'tumor-size', columns = 'Class')['counts']
data_by_class['no-recurrence-events'] = round(100*data_by_class['no-recurrence-events']/data_by_class['no-recurrence-events'].sum(), 1)
data_by_class['recurrence-events'] = round(100*data_by_class['recurrence-events']/data_by_class['recurrence-events'].sum(), 1)

## Plot a stacked bar chart for each age group divided by recurrence
#print(data_by_class)
print(data_by_class)
data_by_class.plot(kind = 'bar', cmap = 'turbo')
plt.title('Distribution Tumor Size in Recurrent Breast Cancer Events')
plt.xlabel("Tumor Size")
plt.ylabel("Percent")
plt.show()

### Visualization 3 ---------------------------------------------------------------------
## Repeat for malignancy designation 
data_by_class = data.groupby('Class')['deg-malig'].value_counts().to_frame('counts')
data_by_class.reset_index(inplace = True)
data_by_class = pd.DataFrame(data_by_class).pivot(index = 'deg-malig', columns = 'Class')['counts']
data_by_class['no-recurrence-events'] = round(100*data_by_class['no-recurrence-events']/data_by_class['no-recurrence-events'].sum(), 1)
data_by_class['recurrence-events'] = round(100*data_by_class['recurrence-events']/data_by_class['recurrence-events'].sum(), 1)

print(data_by_class)
data_by_class.plot(kind = 'bar', cmap = 'turbo')
plt.title('Percent of Recurrent Breast Cancer Events by Malignancy Designation')
plt.xlabel("Malignancy Designation")
plt.ylabel("Percent")
plt.show()

### Visualization 4 -----------------------------------------------------------------------
## This is showing a breakdown of percent of malignancy group that has each tumor size.
## needed iloc for this one because it wasn't recognizing '1' as a string, at least I think that is why.
data_by_malig = data.groupby('deg-malig')['tumor-size'].value_counts().to_frame('counts')
data_by_malig.reset_index(inplace = True)
data_by_malig = pd.DataFrame(data_by_malig).pivot(index = 'tumor-size', columns = 'deg-malig')['counts']
data_by_malig.iloc[1] = round(100*data_by_malig.iloc[1]/data_by_malig.iloc[1].sum(), 1)
data_by_malig.iloc[2] = round(100*data_by_malig.iloc[2]/data_by_malig.iloc[2].sum(), 1)
data_by_malig.iloc[3] = round(100*data_by_malig.iloc[3]/data_by_malig.iloc[3].sum(), 1)

print(data_by_malig)
data_by_malig.plot(kind = 'bar', cmap = 'turbo')
plt.title('Percent of Recurrent Breast Cancer Events by Malignancy Designation')
plt.xlabel("Tumor Size")
plt.ylabel("Percent")
plt.show()