---
title: "Intro to Data Analysis in Python"
schedules:
  dailySchedule: &standardDay
    startTime: "09:00"
    endTime: "17:00"
    breaks:
      - title: Morning Coffee
        doAfter: "10:00"
        minutes: 15
        fixed: false
      - title: Lunch
        doAfter: "11:50"
        minutes: 90
        fixed: true
      - title: Afternoon Coffee
        doAfter: "14:50"
        minutes: 15
        fixed: false
sessions:
  - title: First Day
    foldername: Day1
    schedule: *standardDay
    units:
      - title: First Look
        description: some description
        file: ../../notebooks/FirstLookAtPython.ipynb
        filename: 1-1-IntroToNotebookEnvironment.ipynb
        minutes: 75
      - title: Strings
        file: ../../notebooks/StringsAndMethods.ipynb
        filename: 1-2-MethodsInPython.ipynb
        minutes: 75
  - title: Day 2
    foldername: Day2
    schedule: *standardDay
    units:
      - title: Numpy
        file: ../../notebooks/PlottingData.ipynb
        filename: 2-1-IntroToNumpy.ipynb
        minutes: 75
      - title: Retro
        minutes: 35
---


  # Intro 2 Python

  This is the first course