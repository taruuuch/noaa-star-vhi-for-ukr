# NOAA-Star-VHI-UKR

Simple Python script for work with VHI data, specially for Ukraine provinces

## Dependencies
* Python 3.7.2+
* matplotlib
* numpy

## Description
This Python script working with VHI data, which parsed from NOAA-Star resource.

It perform several functions:
1. Parsing new data from NOAA-Star and saing it in directory **vhi** (VHI by province) and **percent** (VHI by provinence in percents); clearing out odd things in downloaded data files
2. Setting default data set by entering province ID (declared in *list_province* array, line 46 in **Main.py**)
3. Drawing a plot for 1 year, using data from NOAA-Star; using **matplotlib** for graphic engine
4. Drawing a plot for 2 yeary, using data from NOAA-Star; using **matplotlib** for graphic engine
5. Sorting data in **percent** for analyzing anomaly in selected year VHI data (useful for searching "drought" weeks etc.)
