# Data Cleaning
# Data cleaning means fixing bad data in your data set.

# Bad data could be:
# Empty cells
# Data in wrong format
# Wrong data
# Duplicates
# In this tutorial you will learn how to deal with all of them.

# Empty Cells
# Empty cells can potentially give you a wrong result when you analyze data.

# Remove Rows
# One way to deal with empty cells is to remove rows that contain empty cells.

# This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
# ExampleGet your own Python Server
# Return a new Data Frame with no empty cells:

import pandas as pd

df = pd.read_csv('Pandas/data2.csv')

new_df = df.dropna() #Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

print(new_df.to_string())

# If you want to change the original DataFrame, use the inplace = True argument:

# Example
# Remove all rows with NULL values:
# print("=" *100)
# df.dropna(inplace = True) #Note: Now, the dropna(inplace = True) will NOT return a new DataFrame,
#                           #but it will remove all rows containing NULL values from the original DataFrame.
# print(df.to_string())

# Replace Empty Values
# Another way of dealing with empty cells is to insert a new value instead.
# This way you do not have to delete entire rows just because of some empty cells.
# The fillna() method allows us to replace empty cells with a value:

# Example
# Replace NULL values with the number 130:
print("=" *100)
df.fillna(130, inplace = True)

# Replace Only For Specified Columns
# The example above replaces all empty cells in the whole Data Frame.
# To only replace empty values for one column, specify the column name for the DataFrame:

# Example
# Replace NULL alues in the "Calories" columns with the number 130:
print("=" *100)

df["Calories"].fillna(130, inplace = True)
print(df.to_string())

#This operation inserts 130 in empty cells in the "Calories" column (row 18 and 28).

# Replace Using Mean, Median, or Mode
# A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

# Example
# Calculate the MEAN, and replace any empty values with it:
print("=" *100)
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)#Mean = the average value (the sum of all values divided by number of values).
print(x)

# Example
# Calculate the MEDIAN, and replace any empty values with it:
print("=" *100)
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True) #Median = the value in the middle, after you have sorted all values ascending.
print(x)

# Example
# Calculate the MODE, and replace any empty values with it:
print("=" *100)
x = df["Calories"].mode()[0] #Mode = the value that appears most frequently.
df["Calories"].fillna(x, inplace = True)
print(x)
