## PYTHON MATPLOTLIB – LABORATORY STUDY

![Lab_Images](https://i2.imgflip.com/4gr0cs.gif)

### Background
Pymaceuticals company began screening for potential treatments for squamous cell carcinoma (SCC). In this study, 249 mice identified with SCC tumor growth were treated through a variety of drug regimens. Over the course of 45 days, tumor development was observed and measured. The purpose of this study was to compare the performance of Pymaceuticals' drug of interest, Capomulin, versus the other treatment regimens.

### Purpose
Generate a technical report of the study.

### Dataset
- Mouse_metadata.csv
- Study_results.csv

### Description
1. Remove duplicates
2. Generate a summary statistics table consisting of the mean, median, variance, standard deviation, and SEM of the tumor volume for each drug regimen.
3.Generate a bar plot using both Pandas's DataFrame.plot() and Matplotlib's pyplot that shows the number of mice per time point for each treatment regimen throughout the course of the study.
4. Generate a pie plot using both Pandas's DataFrame.plot() and Matplotlib's pyplot that shows the distribution of female or male mice in the study.
5. Calculate the final tumor volume of each mouse across four of the most promising treatment regimens: Capomulin, Ramicane, Infubinol, and Ceftamin. Calculate the quartiles and IQR and quantitatively determine if there are any potential outliers across all four treatment regimens.
6. Using Matplotlib, generate a box and whisker plot of the final tumor volume for all four treatment regimens and highlight any potential outliers in the plot by changing their color and style.
7. Generate a line plot of time point versus tumor volume for a single mouse treated with Capomulin.
8. Generate a scatter plot of mouse weight versus average tumor volume for the Capomulin treatment regimen.
9. Calculate the correlation coefficient and linear regression model between mouse weight and average tumor volume for the Capomulin treatment. Plot the linear regression model on top of the previous scatter plot.




