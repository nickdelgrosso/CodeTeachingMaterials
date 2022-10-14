---
buildFolder: 'build/intro2python'
sessions:
    - units:
      - file: notebooks/FirstLookAtPython.ipynb
        filename: Day1/1-1-IntroToNotebookEnvironment.ipynb
      - file: notebooks/PythonTypes.ipynb
        filename: Day1/1-2-FunctionsAndPythonTypes.ipynb
      - file: notebooks/StringsAndMethods.ipynb
        filename: Day1/1-3-MethodsInPython.ipynb        
      - file: notebooks/DataCollectionsAndFunctions.ipynb
        filename: Day1/1-4-DataCollections.ipynb
      - file: notebooks/PlottingDataWithMatplotlib.ipynb
        filename: Day1/1-5-PlottingWithMatplotlib.ipynb
        
    - units:
      - file: notebooks/NumpyArrays.ipynb
        filename: Day2/2-1-ArraysWithNumpy.ipynb
      - file: notebooks/Logical_Indexing.ipynb
        filename: Day2/2-2-NumpyLogicalIndexing.ipynb
      - file: notebooks/PlottingDistributionsWithNumpyAndMatplotlib.ipynb
        filename: Day2/2-3-PlottingDistributionsWithNumpyAndMatplotlib.ipynb
      - file: notebooks/Multidimensional_Arrays.ipynb
        filename: Day2/2-4-MatricesWithNumpy.ipynb
      - file: notebooks/CroppingAndPlottingImageDataWithMatplotlib.ipynb
        filename: Day2/2-5-BasicImagesWithMatplotlib.ipynb

    - units:
      - file: notebooks/List_Array_Comparison.ipynb
        filename: Day3/3-1-ListArrayComparison.ipynb
      - file: notebooks/TTestsWithScipyStats.ipynb
        filename: Day3/3-2-TtestsWithScipyStats.ipynb
      - file: notebooks/Dictionaries.ipynb
        filename: Day3/3-3-Dictionaries.ipynb
      - file: notebooks/PandasDataframeCreation.ipynb
        filename: Day3/3-4-ReadingTabularFileFormats.ipynb
      - file: notebooks/TTestsWithScipyStatsAndPingouin.ipynb
        filename: Day3/3-5-TTestsWithPingouin.ipynb
      - file: notebooks/AnalyzingDataFrames.ipynb
        filename: Day3/3-6-SelectingAndAggregatingDataframes.ipynb

    - units:
      - file: notebooks/PlottingWithPandas.ipynb
        filename: Day4/4-1-PlottingWithPandas.ipynb
      - file: notebooks/AnalyzingDataFrames.ipynb
        filename: Day4/4-2-SelectingAndAggregatingDataframes.ipynb
      - file: notebooks/Groupby_Seaborn.ipynb
        filename: Day4/4-3-GroupingData.ipynb
      - file: notebooks/ReorganizingDataFrames.ipynb
        filename: Day4/4-4-ReshapingData.ipynb
      
    - units:
      - file: notebooks/FilepathsWithPathlib.ipynb
        filename: Day5/5-1-FindingFilePathsWithPathlib.ipynb
      - file: notebooks/Conda Environment Manager.ipynb
        filename: Day5/5-2-InstallingPythonWithCondaManager.ipynb
      - file: 
      
      
project:
  - LICENSE
  - jupyter_lab_config.py
  - .gitpod.yml
  - .gitignore
git:
  remote-name: origin
  remote-url: git@github.com:CodingForScientists/Intro2Python.git
  remote-branch: master
  

---


# Intro 2 Python

[![Open in Deepnote](https://deepnote.com/buttons/launch-in-deepnote-small.svg)](https://www.deepnote.com/launch?template=data-science&url=https://github.com/CodingForScientists/Intro2Python)

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/CodingForScientists/Intro2Python)

## Schedule

### Day 1

| Approximate Times | Topic |
| :--  | :--   |
| 9:00 -9:30 | Class Orientation |
| 9:30 - 10:15 | Data Science Notebooks Orientation |
| 10:15 - 10:30 | Break |
| 10:30 - 11:45 | Intro to Python's Type System and Key Programming Vocabulary |
| 11:45 - 12:00 | Retrospective |
| 12:00 - 13:30 | Lunch |
| 13:30 - 14:30 | Applying String Methods to Text Analysis |
| 14:30 - 15:45 | Intro to Python's Built-In Data Collection Types and Numpy Arrays |
| 15:45 - 16:00 | Break |
| 16:00 - 16:50 | Basic Plotting with Matplotlib in Data Science Notebooks |
| 16:50 - 17:00 | Retrospective |


### Day 2

| Approximate Times | Topic                                                     |
| :--               | :--                                                       |
| 9:00 - 10:00      | Numpy Arrays                                              |
| 10:00 - 10:15     | Break                                                     |
| 10:15 - 11:00     | Logical Indexing in Numpy                                 |
| 11:00 - 12:00     | Plotting Distributions in Matplotlib                      |
| 12:00 - 13:30     | Lunch                                                     |
| 13:30 - 15:30     | Matrices in Numpy                                         |
| 15:30 - 15:45     | Break                                                     |
| 15:45 - 16:50     | Basic Image Transformations with Numpy and Matplotlib     |
| 16:50 - 17:00     | Retrospective |


### Day 3

| Approximate Times | Topic                                                     |
| :--               | :--                                                       |
| 9:00 - 9:30       | Warm-Up and Orient to VSCode in GitLab : Lists vs Arrays  |
| 9:30 - 10:15      | T-tests on Arrays with Scipy-Stats                        |
| 10:15 - 10:30     | Break                                                     |
| 10:30 - 11:15     | Introduction to Python Dictionaries                       |
| 11:15 - 11:50     | Intro to Pandas DataFrames, Reading and Writing           |
| 11:50 - 12:00     | Recollect and Reflect                                     |
| 12:00 - 13:30     | Lunch                                                     |
| 13:30 - 14:45     | T-tests on DataFrames with Scipy-Stats and Pingouin       |
| 14:45 - 15:00     | Break                                                     |
| 15:00 - 16:50     | DataFrame Selection and Aggregation                       |
| 16:50 - 17:00     | Recollect and Reflect                                     |


### Day 4

| Approximate Times | Topic                                                     |
| :--               | :--                                                       |
| 09:00 - 10:00     | Plotting with Pandas                                      |
| 10:00 - 10:15     | Break                                                     |
| 10:15 - 11:50     | DataFrame Selection and Aggregation                       |
| 11:50 - 12:00     | Recollect and Reflect                                     |
| 12:00 - 13:30     | Lunch                                                     |
| 13:30 - 14:45     | DataFrame GroupBy and Seaborn CatPlot                     |
| 14:45 - 15:00     | Break                                                     |
| 15:00 - 16:50     | Reshaping DataFrames                                      |
| 16:50 - 17:00     | Recollect and Reflect                                     |


### Day 5

| Approximate Times | Topic                                                     |
| :--               | :--                                                       |
| 09:00 - 09:30     | Project Share                                             |
| 09:30 - 10:20     | Filepaths                                                 |
| 10:20 - 10:35     | Break                                                     |
| 10:35 - 11:50     | Installing Python Locally                                 | 
| 11:50 - 12:00     | Recollect and Reflect                                     |
| 12:00 - 13:30     | Lunch                                                     |
| 13:30 - 14:45     | DataFrame GroupBy and Seaborn CatPlot                     |
| 14:45 - 15:00     | Break                                                     |
| 15:00 - 16:50     | Reshaping DataFrames                                      |
| 16:50 - 17:00     | Recollect and Reflect                                     |