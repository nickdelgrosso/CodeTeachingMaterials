---
buildFolder: 'build/intermediatepython'
status: running
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
      include: false
      includeSolutions: false
      units:
        - file: notebooks/DS Pandas Concatenate.ipynb
          filename: Day1/1-4-SplittingAndConcatenatingData.ipynb
        - file:
          filename: Day2/2-1-CategoricalAndParquet.ipynb
        # Stats and Plotting
          - file:
            filename: Day2/Merge
        # Managing Databases
        - file:
          filename: Day2/2-2-SQL_pandas.ipynb

    # # Day 3
    # - title: Statistics and Machine Learning
    #   include: false
    #   includeSolutions: false
    #   units:
      # - file:
      #         filename: Pingouin
    #     # GLM
    #       - file:
    #         filename: Day3/2-3-Fitting One Dimensional Data
    #       - file:
    #         filename: Day3/GLM
    #     # Scikit-Learn: Regression and Clustering
    #     - file:
    #       filename: Day3/Regression
    #     - file:
    #       filename: Day3/Clustering
    
    # # Day 4
    # - title: Neo
    #   include: false
    #   includeSolutions: false
    #   units:

    # # Day 5
    # - title: Statistics and Machine Learning
    #   include: false
    #   includeSolutions: false
    #   units:
    #   - file: # Altair
    #     filename: 
    #   - file: # Streamlit  (which uses altair)
    #     filename: 
    #   - file:   
    #     filename: # IPyWidgets
    #   - file: 
    #     filename: # Panel

    
project:
  - LICENSE
  - jupyter_lab_config.py
  - .gitpod.yml
  - .gitignore
  

---



# Intermediate Python
