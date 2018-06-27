# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 14:11:13 2018  @author: krishna.i
1. Delete unnamed columns
2. Show the distribution of male and female
3. Show the top 5 most preferred names
4. What is the median name occurence in the dataset
5. Distribution of male and female born count by states
"""
#import numpy as np
import pandas as pd

myBabynames = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv", sep=',') 
print(myBabynames.head())

#1. Delete unnamed columns - done with below code
myBabynames.drop(myBabynames.columns[myBabynames.columns.str.contains('Unnamed',case = False)],axis = 1,inplace=True)
print(myBabynames.head())

# 2. Show the distribution of male and female - Done with below code
byGender = myBabynames.groupby('Gender')
print(byGender['Count'].count())

#3. Show the top 5 most preferred names
#byName = myBabynames.groupby('Name')
#topPref = pd.DataFrame(Counter(byName).most_common(5), columns=['Name'])
topPref = myBabynames.groupby(['Name'])['Name'].agg({"Ncount": len}).sort_values("Ncount", ascending=False).head(5).reset_index()

print('The top 5 most preferred names are: ')
print(topPref)
#print(sorted(byName['Name'].count(),order=))

#4. What is the median name occurence in the dataset
byName = myBabynames.groupby('Name')
print('\n\nMedian name occurence in the dataset is: ', byName['Name'].count().median())

#5. Distribution of male and female born count by states
genderDistribn = myBabynames.groupby(['Gender','State'])['Gender'].agg({"Ncount": len}).sort_values("Ncount", ascending=False).reset_index()
print(genderDistribn)
