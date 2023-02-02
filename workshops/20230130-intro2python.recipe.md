---
buildFolder: 'build/intro2python5'
status: running
git:
  sync: true
  branch: main
  remoteName: origin
  remoteURL: https://github.com/CodingForScientists/Intro2PythonLSM2023
readme:
  addDeepnoteShortcut: true
  addGitpodShortcut: true

sessions:
    - title: Intro To Python
      include: true
      includeSolutions: true
      units:
      - file: notebooks/Python First Look.ipynb
        filename: Day1/1-1-IntroToNotebookEnvironment.ipynb
      - file: notebooks/Python Strings And Methods.ipynb
        filename: Day1/1-2-MethodsInPython.ipynb        
      - file: notebooks/Python Data Collections And Functions.ipynb
        filename: Day1/1-3-DataCollections.ipynb
      - file: notebooks/Python Indexing and Slicing.ipynb
        filename: Day1/1-4-IndexingAndSlicingSequences.ipynb
      - file: notebooks/DS Plotting With Matplotlib.ipynb
        filename: Day1/1-5-PlottingWithMatplotlib.ipynb
      - file: notebooks/Python Types.ipynb
        filename: Day1/Extra-FunctionsAndPythonTypes.ipynb
    
    - title: Arrays and Matrices
      include: true
      includeSolutions: true
      units:
      - file: notebooks/DS Numpy Arrays.ipynb
        filename: Day2/2-1-ArraysWithNumpy.ipynb
      - file: notebooks/DS Logical Indexing.ipynb
        filename: Day2/2-2-NumpyLogicalIndexing.ipynb
      - file: notebooks/DS List Array Comparison.ipynb
        filename: Day2/2-3-ListArrayComparison.ipynb
      - file: notebooks/DS Plotting Distributions With Numpy And Matplotlib.ipynb
        filename: Day2/2-4-PlottingDistributionsWithNumpyAndMatplotlib.ipynb
      - file: notebooks/DS Multidimensional Arrays.ipynb
        filename: Day2/2-5a1-MultidimensionalArrays.ipynb
      - file: notebooks/DS Cropping And Plotting Image Data With Matplotlib.ipynb
        filename: Day2/2-5a2-IndexingNDArraysAndCroppingImages.ipynb
      - file: notebooks/DS TTests With Scipy Stats.ipynb
        filename: Day2/2-5b-TTestsWithScipyStats.ipynb

    - title: Dicts and DataFrames
      include: true
      includeSolutions: true
      units:
      - file: notebooks/Python Dictionaries.ipynb
        filename: Day3/3-1-Dictionaries.ipynb
      - file: notebooks/DS Pandas Review MentalRotation.ipynb
        filename: Day3/3-2-DataframesWithPandas.ipynb
      - file: notebooks/DS Analyzing DataFrames.ipynb
        filename: Day3/3-3-SelectingAndAggregatingDataframes.ipynb
      - file: notebooks/DS Groupby Seaborn.ipynb
        filename: Day3/3-4-GroupingData.ipynb
      - file: notebooks/DS Dataframe Creation.ipynb
        filename: Day3/Extra-ReadingTabularFileFormats.ipynb
      
    - title: Data Analysis with DataFrames
      include: true
      includeSolutions: false
      units:
      - file: notebooks/DS Pandas Concatenate.ipynb
        filename: Day4/4-1-ConcatenatingDataframes.ipynb
      - file: notebooks/DS Dataframe Tidy Data Using Melts.ipynb
        filename: Day4/4-2-ReorganizingDataframesWithMelt.ipynb
      - file: notebooks/Python Blocks If Else.ipynb
        filename: Day4/4-3a-IfElseBlocksInPython.ipynb
      - file: notebooks/Python Blocks For Loops.ipynb
        filename: Day4/4-3b-ForLoopsInPython.ipynb
      - file: notebooks/DS Plotnine.ipynb
        filename: Day4/4-3c-PlottingWithPlotnine.ipynb
      - file: notebooks/Python Blocks While Loops.ipynb
        filename: Day4/Extra-WhileLoopsInPython.ipynb
      - file: notebooks/Python Functions.ipynb
        filename: Day4/Extra-FunctionsInPython.ipynb
      - file: notebooks/Misc Filepaths With Pathlib.ipynb
        filename: Day4/Extra-FindingFilePathsWithPathlib.ipynb
        
        
        
      
      
      
project:
  - LICENSE
  - jupyter_lab_config.py
  - .gitpod.yml
  - .gitignore
  

---



# Intro 2 Python

## Schedule

  - **9:30-12:00**: Morning Session w/ 15-Minute Coffee Break
  - **12:00-1:15**: Lunch
  - **1:15-5:00**: Afternoon Session

## Course Plan

  1. **Day 1**: Python's Method Syntax, Numpy Arrays, and Matplotlib Plotting in Deepnote Notebooks
  2. **Day 2**: The Array Structure in Numpy: Multidimensional Arrays
  3. **Day 3**: The DataFrame Structure: Pandas and Seaborn
  4. **Day 4**: Managing Data and Code: Reorganizing Dataframes and Python's Block Syntax