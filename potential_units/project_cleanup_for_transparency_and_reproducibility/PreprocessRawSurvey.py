from random import randint
import numpy as np
import pandas as pd

# Load Data and Rename-and-Realign Columns

df = (
  (df := pd.read_csv('Reproducibilitysurveyrawdata20160523.txt', encoding="ISO-8859-1", delimiter='\t', header=[0, 1]))
  .dropna(axis=1, how='all')
  .rename(columns=lambda s: s+str(randint(1, 100)) if "existing efforts that you've encountered and why" in s else s, level=0)
  .rename(columns=lambda s: np.nan if 'Unnamed' in s else s, level=0)
  .rename(columns=lambda s: '' if 'Unnamed' in s else s, level=1)
)
df.columns = pd.MultiIndex.from_arrays(
    [pd.Series(df.columns.get_level_values(0)).ffill().values,
    df.columns.get_level_values(1).values]
)

# Go through and set dtypes on each column
Go through and set dtypes on each column

def coerce_categorical(ser:pd.Series,categories,ordered=True,likelihood=0.75):
    """Converts Series to Categorical if it contains at least 'likelihood' proportion of category matches."""
    if ser.dropna().astype(str).str.contains('('+'|'.join(categories) + ')$', regex=True).mean() > likelihood:
        return ser.astype(pd.CategoricalDtype(categories, ordered=ordered))
    else:
        return ser
    

df2 = (df
    # Convert int to logical when they just checked an option.
    .apply(lambda ser: ser.astype(bool) if ser.dtype == np.dtype(int) and ser.max() == 1 else ser)
      
    # Convert Strings to Ordered Categorical types when responders were given limited options.
    .apply(coerce_categorical, 
        categories=['Yes', 'No'],
        ordered=False,
        likelihood=0.95)
    .apply(coerce_categorical, 
        categories=['Yes', "I don't know", 'No'],
        likelihood=0.95)
    .apply(coerce_categorical, 
        categories=['Yes', "I am unsure", 'No'],
        likelihood=0.95)
    .apply(coerce_categorical, 
        categories=['Yes', "I can't remember", 'No'],
        likelihood=0.95)
    .apply(coerce_categorical,
        categories=["0%", "10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"],)
    .apply(coerce_categorical, 
        categories=['Not at all familiar', 'Not very familiar', 'Somewhat familiar', 
                    'Fairly familiar', 'Very familiar'])
    .apply(coerce_categorical, 
        categories=['There is no crisis of reproducibility', "I don't know", 
                    'There is a slight crisis of reproducibility', 
                    'There is a significant crisis of reproducibility'])
    .apply(coerce_categorical,
        categories=['Too much', 'A reasonable amount', 'I am unsure', 'Not enough'][::-1],)
    .apply(coerce_categorical,
        categories=[
            '...worse than for other scientific fields on average."',
            'I am unsure',
            '...about the same as for other scientific fields on average"',
           '...better than for other scientific fields on average."',
       ],)
    .apply(coerce_categorical,
       categories=['Within the last year', 'Within the last 2 years',
                   'Within the last 5 years',
                   'The procedures have been in place since I started working in my lab',
                   'Within the last 10 years or longer'],)
    .apply(coerce_categorical,
       categories=['No, the quality of my research has not improved',
                   "I don't know",
                   'Yes, the quality of my research has improved'],)
    .apply(coerce_categorical,
       categories=['These changes have had a negative impact on my lab',
                   'These changes have had a positive impact on my lab',
                   'These changes have not affected my lab'],)
    .apply(coerce_categorical,
        categories=['None', '1-5 members', '6-10 members', '11-25 members', 
                   '26-50 members', 'More than 50 members'], )
    .apply(coerce_categorical,
       categories=['Under 18', '18 - 24', '25 - 34', '35 - 44', 
                   '45 - 54', '55 - 64', '65 or over',], )
    .apply(coerce_categorical,
        categories=['Strongly disagree', 'Disagree', 'Neither agree nor disagree', 
                    'Agree', 'Strongly agree'], )
    .apply(coerce_categorical,
       categories=['Never', 'Daily', 'Weekly', 'Monthly', 'Quarterly'],)
    .apply(coerce_categorical,
       categories=['Never contributes', 'Rarely contributes', "I don't know", 
                   'Sometimes contributes', 'Very often contributes', 'Always contributes'],)
    .apply(coerce_categorical,
        categories=['Not at all likely', 'Not very likely', "I don't know", 
                    'Likely', 'Very likely'], )
      
    # Squeeze multiple sequences of questions into one when the questions went in branching paths.
    .drop(columns=(country_cols := df.filter(regex='country*').columns))
    .assign(**{'Which country do you live in?': df[country_cols].fillna('').apply(''.join, axis=1).replace('', np.nan)})
    .drop(columns=(specialty_cols := df.filter(regex='specialty*').columns))
    .assign(**{
        'What is your specialty?': df[specialty_cols].filter(regex='What is').fillna('').apply(''.join, axis=1).replace('', np.nan),
        'What is your other specialty?': df[specialty_cols].filter(regex='Other').fillna('').apply(''.join, axis=1).replace('', np.nan),
    })
      
    # Make the interview dates Datatimes
    .assign(interview_start=pd.to_datetime(df['interview_start']),
           interview_end=pd.to_datetime(df['interview_end']),
           status=df['status'].astype('category'))
       
    # Set the Index
    .set_index(['responseid', 'respid', 'interview_start', 'interview_end', 'status'])
)


# Seperate sections of the survey
# Each section of the survey will go into its own parquet table, so the categories are preserved and it's easier to find interesting questions.

df.reset_index().iloc[:, :5].to_parquet('../data/processed/ResponseIds.parquet')

df2 = df.reset_index(drop=True)
cols = df2.columns.get_level_values(0).unique()[:2]
df2[cols].to_parquet('../data/processed/current_role.parquet')
cols = df2.columns.get_level_values(0).unique()[2:7]
df2[cols].to_parquet('../data/processed/crisis_of_reproducibility.parquet')
cols = df2.columns.get_level_values(0).unique()[7:11]
df2[cols].to_parquet('../data/processed/failure_to_reproduce.parquet')
cols = df2.columns.get_level_values(0).unique()[11:12]
df2[cols].to_parquet('../data/processed/interest_in_reproducibility.parquet')
cols = df2.columns.get_level_values(0).unique()[12:17]
df2[cols].to_parquet('../data/processed/funding_and_journal_efforts.parquet')
cols = df2.columns.get_level_values(0).unique()[17:25]
df2[cols].to_parquet('../data/processed/efforts_to_reproduce.parquet')
# cols = df2.columns.get_level_values(0).unique()[14:35]
# df2[cols].to_parquet('../data/processed/interestingquestions.parquet')
cols = df2.columns.get_level_values(0).unique()[25:32]
df2[cols].to_parquet('../data/processed/barriers_to_reproducibility.parquet')
cols = df2.columns.get_level_values(0).unique()[32:35]
df2[cols].to_parquet('../data/processed/experiences_reproducing_results.parquet')
cols = df2.columns.get_level_values(0).unique()[35:]
df2[cols].to_parquet('../data/processed/person.parquet')



