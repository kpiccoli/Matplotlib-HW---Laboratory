#!/usr/bin/env python
# coding: utf-8

# ## Observations and Insights 

# 

# In[48]:


get_ipython().run_line_magic('matplotlib', 'inline')

# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
import numpy as np

# Study data files
mouse_metadata_path = "data/Mouse_metadata.csv"
study_results_path = "data/Study_results.csv"

# Read the mouse data and the study results
mouse_metadata = pd.read_csv(mouse_metadata_path)
study_results = pd.read_csv(study_results_path)

# Combine the data into a single dataset
lab_df = pd.merge(mouse_metadata, study_results, on="Mouse ID", how="outer")
lab_df.head()


# In[49]:


mouse_metadata


# In[50]:


lab_df.info()


# In[51]:


# Checking the number of mice in the DataFrame.
mouse_count = len(lab_df["Mouse ID"].unique())
mouse_count


# In[52]:


# Getting the duplicate mice by ID number that shows up for Mouse ID and Timepoint. 
dup_mice = lab_df.loc[lab_df.duplicated(subset=["Mouse ID", "Timepoint"]), "Mouse ID"].unique()
dup_mice


# In[53]:


# Optional: Get all the data for the duplicate mouse ID. 
dup_data = lab_df.loc[lab_df["Mouse ID"]=="g989"]
dup_data


# In[54]:


# Create a clean DataFrame by dropping the duplicate mouse by its ID.
clean_df = lab_df[lab_df["Mouse ID"].isin(dup_mice)==False]
clean_df


# In[55]:


# Checking the number of mice in the clean DataFrame.
len(clean_df["Mouse ID"].unique())


# ## Summary Statistics

# In[56]:


# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen
# This method is the most straighforward, creating multiple series and putting them all together at the end.

sum_stats = pd.DataFrame(clean_df.groupby("Drug Regimen").count())

sum_stats["Mean"] = pd.DataFrame(clean_df.groupby("Drug Regimen")["Tumor Volume (mm3)"].mean())
sum_stats["Median"] = pd.DataFrame(clean_df.groupby("Drug Regimen")["Tumor Volume (mm3)"].median())
sum_stats["Variance"] = pd.DataFrame(clean_df.groupby("Drug Regimen")["Tumor Volume (mm3)"].var())
sum_stats["Standard Deviation"] = pd.DataFrame(clean_df.groupby("Drug Regimen")["Tumor Volume (mm3)"].std())
sum_stats["SEM"] = pd.DataFrame(clean_df.groupby("Drug Regimen")["Tumor Volume (mm3)"].sem())

sum_stats = sum_stats[["Mouse ID","Mean", "Median", "Variance", "Standard Deviation", "SEM"]]
sum_stats = sum_stats.sort_values("Mean", ascending=True)
sum_stats


# ## Bar Plots

# In[57]:


# Generate a bar plot showing the number of mice per time point for each treatment throughout the course of the study using pandas.
x_axis = clean_df["Drug Regimen"].value_counts()
x_axis
x_axis.plot(kind="bar")
plt.xlabel("Drug Regimen")
plt.ylabel("Number of Mice")
plt.show()


# In[58]:


# Generate a bar plot showing the number of mice per time point for each treatment throughout the course of the study using pyplot.
x_axis = clean_df["Drug Regimen"].value_counts()
plt.bar(x_axis.index.values, x_axis.values)
plt.xticks(rotation=90)
plt.xlabel("Drug Regimen")
plt.ylabel("Number of Mice")
plt.show()


# ## Pie Plots

# In[59]:


# Generate a pie plot showing the distribution of female versus male mice using pandas
gender_count = mouse_metadata.Sex.value_counts()
gender_count
gender_count.plot(kind="pie", autopct="%1.1f%%", startangle=140, shadow=True, fontsize=14, title= "Distribuition of Female versus Male mice")
plt.show()


# In[60]:


# Generate a pie plot showing the distribution of female versus male mice using pyplot
gender_count = mouse_metadata.Sex.value_counts()
plt.pie(gender_count.values, labels=gender_count.index.values, autopct="%1.1f%%", startangle=140, shadow=True)
plt.ylabel("Sex")
plt.title("Distribuition of Female versus Male mice")
plt.show()


# ## Quartiles, Outliers and Boxplots

# In[61]:


# Calculate the final tumor volume of each mouse across four of the most promising treatment regimens. Calculate the IQR and quantitatively determine if there are any potential outliers. 
sum_stats.head(4)


# In[83]:


#Create a list of the four drugs and a subset data frame
four_drugs_list = ["Ramicane", "Capomulin", "Propriva", "Ceftamin"]
four_drugs = clean_df[clean_df["Drug Regimen"].isin(four_drugs_list)]
four_drugs.head()


# In[84]:


#Determine if there are any potencial outliers
quartiles = four_drugs['Tumor Volume (mm3)'].quantile([.25,.5,.75])
lowerq = quartiles[0.25]
upperq = quartiles[0.75]
iqr = upperq - lowerq

print(f"The lower quartile Tumor Volume is: {lowerq}")
print(f"The upper quartile Tumor Volume is: {upperq}")
print(f"The interquartile range Tumor Volume is: {iqr}")
print(f"The the median Tumor Volume is: {quartiles[0.5]} ")

lower_bound = lowerq - (1.5*iqr)
upper_bound = upperq + (1.5*iqr)
print(f"Values below {lower_bound} could be outliers.")
print(f"Values above {upper_bound} could be outliers.")


# In[90]:


# Generate a box plot of the final tumor volume of each mouse across four regimens of interest
Tumor_Volume = four_drugs['Tumor Volume (mm3)']
fig1, ax1 = plt.subplots()
ax1.set_title('Tumor Volume of Mice')
ax1.set_ylabel('Tumor Volume')
ax1.boxplot(Tumor_Volume)
plt.show()


# ## Line and Scatter Plots

# In[92]:


# Generate a line plot of time point versus tumor volume for a mouse treated with Capomulin

# Filter original data for just the Capomulin Drug Regime
Capomulin_df = clean_df.loc[(clean_df["Drug Regimen"] == "Capomulin"),:]

# Set variables to hold relevant data
timepoint = Capomulin_df["Timepoint"]
tumor_volume = Capomulin_df["Tumor Volume (mm3)"]

# Plot the tumor volume for various mice
tumor_volume_line, = plt.plot(timepoint, tumor_volume)

# Show the chart, add labels
plt.xlabel('Timepoint')
plt.ylabel('Tumor Volume')
plt.title('Tumor Volume over Time for Capomulin Mice')
plt.show()


# In[93]:


# Generate a scatter plot of mouse weight versus average tumor volume for the Capomulin regimen

# Pull values for x and y values
mouse_weight = Capomulin_df.groupby(Capomulin_df["Mouse ID"])["Weight (g)"].mean()
tumor_volume = Capomulin_df.groupby(Capomulin_df["Mouse ID"])["Tumor Volume (mm3)"].mean()

# Create Scatter Plot with values calculated above
plt.scatter(mouse_weight,tumor_volume)
plt.xlabel("Weight of Mouse")
plt.ylabel("Tumor Volume")
plt.show()


# ## Correlation and Regression

# In[94]:


# Calculate the correlation coefficient and linear regression model 
# for mouse weight and average tumor volume for the Capomulin regimen

# Pull values for x and y values
mouse_weight = Capomulin_df.groupby(Capomulin_df["Mouse ID"])["Weight (g)"].mean()
tumor_volume = Capomulin_df.groupby(Capomulin_df["Mouse ID"])["Tumor Volume (mm3)"].mean()

# Perform a linear regression on year versus violent crime rate
slope, int, r, p, std_err = st.linregress(mouse_weight, tumor_volume)
      
# Create equation of line to calculate predicted violent crime rate
fit = slope * mouse_weight + int

# Plot the linear model on top of scatter plot 
plt.scatter(mouse_weight,tumor_volume)
plt.xlabel("Weight of Mouse")
plt.ylabel("Tumor Volume")
plt.plot(mouse_weight,fit,"--")
plt.xticks(mouse_weight, rotation=90)
plt.show()

# Caculate correlation coefficient
corr = round(st.pearsonr(mouse_weight,tumor_volume)[0],2)
print(f'The correlation between weight and tumor value is {corr}')


# In[ ]:





# In[ ]:





# In[ ]:




