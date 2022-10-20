import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load Data
person = pd.read_parquet('persooon.parquet')
crisis = pd.read_parquet('crisis_of_reproducibility.parquet')
df = pd.merge(person, crisis, left_index=True, right_index=True)  # Merge two dataframes into a single dataset


# Analysis

#Get all job titles
sns.countplot(y=df['Which of the following job titles best applies to you?'])
plt.savefig('jobtitles.png');

# Specialties
plt.figure(figsize=(5, 20))
sns.countplot(y=df['What is your specialty?']);
plt.savefig('specialties.png')


# Filter out Biologists
specialty='Biology'
mask=df['What is your specialty?'].str.contains(specialty)&df['What is your specialty?'].notnull()
sns.countplot(y=df['Which of the following job titles best applies to you?'][mask])
plt.title(specialty)
plt.savefig('biologist_specialties.png')


# Get Biologists opinion on crisis
question = 'Which of the following statement regarding a\xa0\'crisis or reproducibility\' within the science community\xa0do you agree with?'
sns.countplot(y=df[question][mask])
plt.title(question)
plt.savefig('biologist_feeling_on_crisis.png')


