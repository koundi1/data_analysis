# -*- coding: utf-8 -*-
"""Matplotlib and Seaborn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HvJmBrQqGxYw2FL_VqTPwP_67eLVz0_K
"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

#line chart - here is a python list showing yield of applies (tons per hectare) over six years in an imaginary country called kanto
yield_apples = [0.895, 0.91, 0.919, 0.926,0.929, 0.931]
#to draw a line chart we use plt.plot function
plt.plot(yield_apples)

# the x axis on the test data shows elements 0 to 5. We can replace this data with year by adding another argument on plt.plot()
yield_apples = [0.895, 0.91, 0.919, 0.926,0.929, 0.931]
years = [2010,2011, 2012, 2013, 2014, 2015]
plt.plot(years, yield_apples)

#adding axis labels
# we can add labels to the axis with the plt.xlabels and plt.ylabels methods.
plt.plot(years, yield_apples)
plt.xlabel('Year')
plt.ylabel('Yield, tons per hectare')

# plotting multiple lines
#We can plot multiple lines using the plt.plot method
years = range(2000,2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
plt.plot(years, apples)
plt.plot(years, oranges)
plt.xlabel('Year')
plt.ylabel('Yield, ton per hectare')

# Chart title and legend
# We can include a legend using plot.legend function and create a title using plot.title function
plt.plot(years, apples)
plt.plot(years, oranges)

plt.xlabel('Year')
plt.ylabel('Yield - ton per hectare')

plt.legend(['Apples', 'Oranges'])
plt.title('fruit yield in kanto')

#line markers - we can show markers for the data points using the marker argument in plt.plot
plt.plot(years, apples, marker = 'o')
plt.plot(years, oranges, marker = 'x')

plt.xlabel('Year')
plt.ylabel('Yield - ton per hectare')

plt.title('Fruit yield in Kanto')
plt.legend(['Apples', 'Oranges'])



"""Styling Lines and Markers
The plt.plot function supports many arguments for styling lines and markers:

color or c: Set the color of the line (supported colors)
linestyle or ls: Choose between a solid or dashed line
linewidth or lw: Set the width of a line
markersize or ms: Set the size of markers
markeredgecolor or mec: Set the edge color for markers
markeredgewidth or mew: Set the edge width for markers
markerfacecolor or mfc: Set the fill color for markers
alpha: Opacity of the plot

"""

plt.plot(years, apples, marker='s', c='b', ls='-', lw=2, ms=8, mew=2, mec='navy')
plt.plot(years, oranges, marker='o', c='r', ls='--', lw=3, ms=10, alpha=.5)

plt.xlabel('Year')
plt.ylabel('Yield - ton per hectare')

plt.title('crop yields in kanto')
plt.legend(['Apples', 'Oranges'])

#The `fmt` argument provides a shorthand for specifying the marker shape, line style, and line color. It can be provided as the third argument to `plt.plot. fmt = '[marker][line][color]'
plt.plot(years, apples, 's-b')
plt.plot(years, oranges, 'o--r')

plt.xlabel('Year')
plt.ylabel('Yield in ton per hectare')

plt.title('Crop yeild in kanto')
plt.legend(['Apples', 'Oranges'])

#if we dont specify fmt, only markers are drawn
plt.plot(years, apples, 'or')
plt.title('Orange yield in ton per hectare')

#changing hte figure size
plt.figure(figsize = (12,6))
plt.plot(years, apples)
plt.title('Yield in ton per hectare')

# improving default styles using seaborn
#use sns.set_style to make the charts look beautiful

sns.set_style('whitegrid')

plt.plot(years, apples, 's-b')
plt.plot(years, oranges, 'o--r')

plt.xlabel('year')
plt.ylabel('Yield in ton per hectare')

plt.title('Crop yield in kanto')
plt.legend(['Apples', 'Oranges'])

#usign darkgrid

sns.set_style('darkgrid')

plt.plot(years, apples, 's-b')
plt.plot(years, oranges, 'o--r')

plt.xlabel('Year')
plt.ylabel('Yield in ton per hectare')

plt.title('Crop yield in kanto')
plt.legend(['apples', 'oranges'])

plt.plot(years, oranges, 'or')
plt.title('Yield for oranges in Kanto')

#loading data set in pandas dataframe
flowers_df = sns.load_dataset('iris')

flowers_df

flowers_df.species.unique()

#lets plot hte relatuonship between speal lenght and sepal width
plt.plot(flowers_df.sepal_length, flowers_df.sepal_width, 'or')

#using scatterplot function
sns.scatterplot(x =flowers_df.sepal_length, y = flowers_df.sepal_width)

#Adding hues
sns.scatterplot(x = flowers_df.sepal_length, y = flowers_df.sepal_width,hue = flowers_df.species, s= 50)

#seaborn uses matplot lib plotting functions like plt.title and plt.figure.
plt.figure(figsize=(12,5))
plt.title('Sepal Dims')

sns.scatterplot(x = flowers_df.sepal_length, y = flowers_df.sepal_width, hue = flowers_df.species, s = 50)

#plotting using pandas dataframe
plt.title("Sepal Dimensions")
sns.scatterplot(data = flowers_df, x = 'sepal_length', y = 'sepal_width', hue = 'species', s= 50)

#load dataset into a pandas dataframe
flowers_df = sns.load_dataset('iris')
flowers_df

flowers_df.sepal_width

#plot a histogram for sepal width
plt.title('Frequency of Sepal Width')
plt.hist(flowers_df.sepal_width)

#We can control the size of the histogram with the bins arguments
plt.hist(flowers_df.sepal_width, bins = 5)

import numpy as np
plt.hist(flowers_df.sepal_width, bins = np.arange(2,5,0.25))

#bins of unequal sizes
plt.hist(flowers_df.sepal_width, bins = [1,3,4,4.5])

#Multiple Histograms
setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']

setosa_df

setosa_df.sepal_width

plt.hist(setosa_df.sepal_width, alpha = 0.4, bins = np.arange(2,5,0.25))
plt.hist(versicolor_df.sepal_width, alpha = 0.4, bins = np.arange(2,5,0.25))

#we cn also stack multimple histograms on top of one another
plt.hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width], bins = np.arange(2,5,0.25), stacked = True)
plt.legend(['Setosa', 'Versicolor', 'Virginica'])

#Bar Chart
year = range(2000, 2006)
apples = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
oranges = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]
plt.bar(year, oranges)

#bar chart stacking
plt.bar(year, apples)
plt.bar(year, oranges, bottom = apples)

#bar plot with averages

"""Let's look at another sample dataset included with Seaborn, called tips. The dataset contains information about the sex, time of day, total bill, and tip amount for customers visiting a restaurant over a week."""

tips_df = sns.load_dataset('tips')
tips_df

#bar plot under seaborn library computes the average
sns.barplot(x = 'day', y='total_bill', data= tips_df)

sns.barplot(x = 'day', y = 'total_bill', hue = 'sex', data = tips_df)

#horizontal bars
sns.barplot(x='total_bill', y = 'day', hue='sex', data = tips_df)

#heatmap
#load a dataseet named flights to visualize monthly passenger footfall in an aiport over 12 years

flights_df = sns.load_dataset('flights').pivot('month', 'year', 'passengers')
flights_df

#we will use sns.heatmap fucntion to visualize the footprint
plt.title('No of Passengers (1000s)')
sns.heatmap(flights_df)

#we can also display the actual values by specifying annot = True and changing the color pallete
plt.title("No of Passengers (1000s)")
sns.heatmap(flights_df, fmt = 'd', annot = True, cmap = 'Blues' )

#Images
#We can use matplot lib ro display images

from urllib.request import urlretrieve
urlretrieve('https://i.imgur.com/SkPbq.jpg', 'chart.jpg')

from PIL import Image

img = Image.open('chart.jpg')

#we can convert image into an array using numpy array. this array contains pixes for red green and blue channels
img_array = np.array(img)
img_array.shape

plt.imshow(img)

#turn off the axis and grid
plt.grid(False)
plt.title("A data science meme")
plt.axis('off')
plt.imshow(img)

#to display a part of the image, we can select a slice of the numpy array
plt.grid(False)
plt.axis('off')
plt.imshow(img_array[125:325, 105:305])

"""Plotting multiple charts in a grid using plt.subplots()"""

fig, axes = plt.subplots(2,3, figsize=(16,8))

#use the axes for plotting
axes[0,0].plot(year, apples, 's-b')
axes[0,0].plot(year, oranges,'o--r')
axes[0,0].set_xlabel('Year')
axes[0,0].set_ylabel('Yield in tons per hectare')
axes[0,0].set_title('Crop yield in kanto')
axes[0,0].legend(['Apples', 'Oranges'])



#pass the axes into seaborn
axes[0,1].set_title('Sepal Length vs Sepal Width')
sns.scatterplot(x = flowers_df.sepal_length, y = flowers_df.sepal_width, hue = flowers_df.species, s= 100, ax = axes[0,1])





#use the axes for plotting
axes[0,2].set_title('Distribution of sepal width')
axes[0,2].hist([setosa_df.sepal_length, versicolor_df.sepal_length, virginica_df.sepal_length])#bins = np.arange(2.5,0.25), stacked=True)
axes[0,2].legend(['setosa', 'versicolor','virginica'])


#pass the axes into seaborn
axes[1,1].set_title('flight traffic')
sns.heatmap(flights_df, cmap = 'Blues', ax = axes[1,1])



#pass the axes into seaborn
axes[1,0].set_title('Restaurant bills')
sns.barplot(x = 'day', y ='total_bill', hue = 'sex', data = tips_df, ax=axes[1,0])


#plot an image using the axes
axes[1,2].set_title('A data science meme')
axes[1,2].imshow(img)
axes[1,2].grid(False)
axes[1,2].set_xticks([])
axes[1,2].set_yticks([])

plt.tight_layout(pad=2)

