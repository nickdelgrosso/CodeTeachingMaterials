---
buildFolder: 'build/intermediatepython'
status: finished
git:
  sync: true
  branch: main
  remoteName: origin
  remoteURL: https://github.com/CodingForScientists/IntermediatePythonMPI2022
readme:
  addDeepnoteShortcut: false
  addGitpodShortcut: true

sessions:

    # Day 1
    - title: Pandas and Multiple Files
      include: true
      includeSolutions: true
      units:

      # DataFrames
      - file: notebooks/Python Lists and String Formatting.ipynb
        filename: Day1/1-1-PythonReviewListsStringFormatting.ipynb
      - file: notebooks/Python Blocks For Loops 2.ipynb
        filename: Day1/1-2-ForLoops.ipynb     

      # Managing Many Files, Importance of IDs
      - file: notebooks/DS Pandas Review MentalRotation.ipynb
        filename: Day1/1-3-PandasReview.ipynb
      
      
    # Day 2
    - title: Relational Data, Shrinking the Analysis Pipeline
      include: true
      includeSolutions: true
      units:
        - file: notebooks/DS Pandas Concatenate.ipynb
          filename: Day2/2-1-SplittingAndConcatenatingDataFramesInLoops.ipynb
        - file: notebooks/DS DataFrame Merging Columns.ipynb
          filename: Day2/2-2-MergingDataFrames.ipynb
        - file: notebooks/DS Intro To SQL.ipynb
          filename: Day2/2-3-SQL_pandas.ipynb

    # # Day 3
    - title: Tidy Data, Statistics and Machine Learning
      include: true
      includeSolutions: true
      units:
        # Plotting
        - file: notebooks/DS Seaborn2.ipynb
          filename: Day3/3-1-PlottingWithSeaborn.ipynb
        - file: notebooks/DS Plotnine.ipynb
          filename: Day3/3-2-PlottingWithPlotnine.ipynb
        - file: notebooks/DS Dataframe Tidy Data Using Melts.ipynb
          filename: Day3/3-3-TidyingDataWithPandasMelt.ipynb
        - file: notebooks/DS Fitting One Dimensional Data.ipynb
          filename: Day3/3-4-FittingDistributionsWithScipyStats.ipynb



          
    
    #       - file:
    #         filename: 
    #       - file:
    #         filename: Day3/GLM
    #     # Scikit-Learn: Regression and Clustering
    #     - file:
    #       filename: Day3/Regression
    #     - file:
    #       filename: Day3/Clustering
    
    # Day 4
    - title: Functions, GLM, and Neo
      include: true
      includeSolutions: true
      units:
        - file: notebooks/DS Fitting One Dimensional Data.ipynb
          filename: Day4/4-1-FittingDistributionsWithScipyStats.ipynb

    # Day 5
    - title: Statistics and Machine Learning
      include: true
      includeSolutions: true
      units:
      - file: notebooks/DS TTests with Pingouin.ipynb
        filename:  Day5/5-1-TtestsWithPingouin.ipynb
      - file: notebooks/Python Functions.ipynb
        filename: Day5/5-2-DefiningPythonFunctions.ipynb
      - file: notebooks/DS GLM with Pingouin And Statsmodels.ipynb
        filename: Day5/5-3-GLMwithPinguoinAndStatsmodels.ipynb
      - file: notebooks/DS Machine Learning With ScikitLearn.ipynb
        filename: Day5/5-4-MachineLearningWithScikitLearn.ipynb
      

    
project:
  - LICENSE
  - jupyter_lab_config.py
  - .gitpod.yml
  - .gitignore
  

---



# Intermediate Python
