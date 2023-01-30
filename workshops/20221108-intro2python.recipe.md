---
buildFolder: 'build/intro2python3'
status: finished
git:
  sync: true
  branch: main
  remoteName: origin
  remoteURL: https://github.com/CodingForScientists/Intro2PythonMPI2022
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
      - file: notebooks/Python Types.ipynb
        filename: Day1/1-2-FunctionsAndPythonTypes.ipynb
      - file: notebooks/Python Strings And Methods.ipynb
        filename: Day1/1-3-MethodsInPython.ipynb        
      - file: notebooks/Python Data Collections And Functions.ipynb
        filename: Day1/1-4-DataCollections.ipynb
      - file: notebooks/DS Plotting With Matplotlib.ipynb
        filename: Day1/1-5-PlottingWithMatplotlib.ipynb
    
    - title: Arrays and Matrices
      include: true
      includeSolutions: true
      units:
      - file: notebooks/Python Indexing and Slicing.ipynb
        filename: Day2/2-1-IndexingAndSlicingSequences.ipynb
      - file: notebooks/DS List Array Comparison.ipynb
        filename: Day2/2-2-ListArrayComparison.ipynb
      - file: notebooks/DS Numpy Arrays.ipynb
        filename: Day2/2-3-ArraysWithNumpy.ipynb
      - file: notebooks/DS Logical Indexing.ipynb
        filename: Day2/2-4-NumpyLogicalIndexing.ipynb
      - file: notebooks/DS Plotting Distributions With Numpy And Matplotlib.ipynb
        filename: Day2/2-5-PlottingDistributionsWithNumpyAndMatplotlib.ipynb

    - title: Dicts and DataFrames
      include: true
      includeSolutions: true
      units:
      - file: notebooks/DS Multidimensional Arrays.ipynb
        filename: Day3/3-1-MultidimensionalArrays.ipynb
      - file: notebooks/DS Cropping And Plotting Image Data With Matplotlib.ipynb
        filename: Day3/3-2-IndexingNDArraysAndCroppingImages.ipynb
      - file: notebooks/DS TTests With Scipy Stats.ipynb
        filename: Day3/3-3-ComparingMultipleVariables.ipynb
      

    - title: Data Analysis with DataFrames
      include: true
      includeSolutions: true
      units:
      - file: notebooks/Python Dictionaries.ipynb
        filename: Day4/4-1-Dictionaries.ipynb
      - file: notebooks/DS Dataframe Creation.ipynb
        filename: Day4/4-2-ReadingTabularFileFormats.ipynb
      - file: notebooks/DS Analyzing DataFrames.ipynb
        filename: Day4/4-3-SelectingAndAggregatingDataframes.ipynb
      - file: notebooks/DS Groupby Seaborn.ipynb
        filename: Day4/4-4-GroupingData.ipynb
    
    - title: Batch Data Processing
      include: true
      includeSolutions: true
      units:
      - file: notebooks/Misc Filepaths With Pathlib.ipynb
        filename: Day5/5-1-FindingFilePathsWithPathlib.ipynb
      - file: notebooks/Python Blocks If Else.ipynb
        filename: Day5/5-2-IfElseBlocksInPython.ipynb
      - file: notebooks/Python Blocks While Loops.ipynb
        filename: Day5/5-3-WhileLoopsInPython.ipynb
      - file: notebooks/Python Blocks For Loops.ipynb
        filename: Day5/5-4-ForLoopsInPython.ipynb
      
      
      
project:
  - LICENSE
  - jupyter_lab_config.py
  - .gitpod.yml
  - .gitignore
  

---



# Intro 2 Python
