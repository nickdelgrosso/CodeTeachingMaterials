---
buildFolder: 'build/intro2python4'
status: running
git:
  sync: true
  branch: main
  remoteName: origin
  remoteURL: https://github.com/CodingForScientists/Intro2PythonTuebingen2022
readme:
  addDeepnoteShortcut: true
  addGitpodShortcut: true

sessions:
    - title: Intro to Python's Syntax and Data Science Notebooks
      include: true
      includeSolutions: true
      units:

      # In-Class
      - file: notebooks/Python First Look.ipynb
        filename: Week1/1-1-IntroToNotebookEnvironment.ipynb
      - file: notebooks/Python Types.ipynb
        filename: Week1/1-2-FunctionsAndPythonTypes.ipynb
      - file: notebooks/Python Strings And Methods.ipynb
        filename: Week1/1-3-MethodsInPython.ipynb   

      # Homework
      - file: notebooks/Python Data Collections And Functions.ipynb
        filename: Week1/1-4-Homework-DataCollections.ipynb

    - title: Numpy Arrays and Plotting with Matplotlib
      include: true
      includeSolutions: true
      units:
      # In-Class
      - file: notebooks/Python Indexing and Slicing.ipynb
        filename: Week2/2-1-IndexingAndSlicingSequences.ipynb
      - file: notebooks/DS Numpy Arrays.ipynb
        filename: Week2/2-2-ArraysWithNumpy.ipynb
      - file: notebooks/DS Plotting With Matplotlib.ipynb
        filename: Week2/2-3-PlottingWithMatplotlib.ipynb
      
      # Homework
      - file: notebooks/DS List Array Comparison.ipynb
        filename: Week2/2-4-Reference-ListArrayComparison.ipynb
      - file: notebooks/DS Logical Indexing.ipynb
        filename: Week2/2-5-Homework-NumpyLogicalIndexing.ipynb
      
      
      
    
    - title: Multidimensional Arrays and Statistics with Scipy-Stats
      include: true
      includeSolutions: true
      units:
      # In-Class
      - file: notebooks/DS Plotting Distributions With Numpy And Matplotlib.ipynb
        filename: Week3/3-1-PlottingDistributionsWithNumpyAndMatplotlib.ipynb
      - file: notebooks/DS Multidimensional Arrays.ipynb
        filename: Week3/3-2-MultidimensionalArrays.ipynb
      - file: notebooks/DS Cropping And Plotting Image Data With Matplotlib.ipynb
        filename: Week3/3-3-IndexingNDArraysAndCroppingImages.ipynb
      
        # Homework
      - file: notebooks/DS TTests With Scipy Stats.ipynb
        filename: Week3/3-4-Homework-TtestsWithScipyStats.ipynb
      - file: notebooks/Python Dictionaries.ipynb
        filename: Week3/3-5-Homework-Dictionaries.ipynb
      

      

    - title: Data Analysis with DataFrames
      include: true
      includeSolutions: true
      units:
        # In-Class
      - file: notebooks/DS Analyzing DataFrames.ipynb
        filename: Week4/4-1-SelectionAndAggregation.ipynb
      - file: notebooks/DS Groupby Seaborn.ipynb
        filename: Week4/4-2-GroupingData.ipynb
      - file: notebooks/DS DataFrame Reorganizing.ipynb
        filename: Week4/4-3-ReshapingData.ipynb

        # Homework
      - file: notebooks/DS Dataframe Creation.ipynb
        filename: Week4/4-Homework-ReadingTabularFileFormats.ipynb
      - file: notebooks/Misc Filepaths With Pathlib.ipynb
        filename: Week4/4-Homework-FindingFilePathsWithPathlib.ipynb
      
      
      
    
    
    - title: Batch Data Processing
      include: true
      includeSolutions: false
      units:
      - file: notebooks/SE Conda Environment Manager.ipynb
        filename: Week5/5-Ref-InstallingPythonWithCondaManager.ipynb
      - file: notebooks/DS Pandas Review MentalRotation.ipynb
        filename: Week5/5-1-PandasReview.ipynb
      
      # Homework
      - file: notebooks/Misc Filepaths With Pathlib.ipynb
        filename: Week5/5-2-FindingFilePathsWithPathlib.ipynb
      - file: notebooks/Python Blocks If Else.ipynb
        filename: Week5/5-3-IfElseBlocksInPython.ipynb
      - file: notebooks/Python Blocks For Loops.ipynb
        filename: Week5/5-4-ForLoopsInPython.ipynb
      
    - title: Putting it all together into an analysis
      include: false
      includeSolutions: false


      
project:
  - LICENSE
  - jupyter_lab_config.py
  - .gitpod.yml
  - .gitignore
  

---



# Intro 2 Python

## Course Design

  
  - **Hands-On Exercises**: This is a hands-on course, with at least 50% of in-class time spent in small groups.  In each 3.5-hour session, we'll have cover 2-3 topics around a central unit, working in small groups to complete exercise problems in a data science notebook.  Two additional worksheet notebooks (~90-120 minutes of work) designed to flesh out the topic covered or to prepare you for the next week will need to be done outside of class time.  

  - **Programming Platform**: There are a wide variety of analysis platforms we can use to to program in Python.  In this course, we will learn 4 different platforms: 
    1. Deepnote
    2. VS Code Web in GitPod
    3. Jupyter Lab with Conda
    4. VS Code Desktop with Conda

  - **BYOD (Bring Your Own Data)**: On the final day of the course, we will analyze one of our own datasets.  The rest of the course we will use prepared data supplied by the instructor, or generate our own (in cases of simulated data).

  - **All People Are the Right People, All Questions Are Good Questions, All Directions Are Good Directions**: The course may go in different directions based on the interests and questions of the group. That's just fine!  There is an endless amount of material for us to learn in data analysis; we'll learn as much as we can about as much as we can.

## Course Plan

  1. **Python's Syntax and Data Science Notebooks with DeepNote**: *Nov 21, 2022 09:00 AM - 12:30 PM*
  
  2. **Numpy Arrays and Plotting with Matplotlib**: *Nov 28, 2022 09:00 AM - 12:30 PM*

  3. **Multidimensional Arrays and Statistics with Scipy-Stats**: *Dec 5, 2022 09:00 AM - 12:30 PM*

  4. **Tabular Data Analysis with Pandas DataFrames and Seaborn Statistical Plotting**: *Dec 12, 2022 09:00 AM - 12:30 PM*

  5. **Batch Data Analysis: Programming a Workflow**: *Jan 16, 2023 09:00 AM - 12:30 PM*

  6. **Bringing it All Together: Analyzing Your Own Data On Your Own Computer**: *Jan 23, 2023 09:00 AM - 12:30 PM*