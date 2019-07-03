#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'quizzes'))
	print(os.getcwd())
except:
	pass

#%%
import pandas as pd
import numpy as np

df = pd.read_csv('titanic.csv')


#%%



#%%
c_pass = len(df[df["Embarked"] == 'C'])


#%%
total = len(df["Embarked"])


#%%
c_pass/total


#%%
female_tot_at_c = len((df[(df['Sex'] == 'female') & (df['Embarked'] == 'C')]))


#%%
female_tot_at_c/c_pass


#%%
tot_fem = len(df[df['Sex'] == 'female'])


#%%
female_tot_at_c/tot_fem


#%%





#%%
