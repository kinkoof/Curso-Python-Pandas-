# # What is a Series?
# A Pandas Series is like a column in a table.

# It is a one-dimensional array holding data of any type.

# Create a simple Pandas Series from a list:
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

# Labels
# If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

# This label can be used to access a specified value.

# Example:
print("=" *30)

print(myvar[0])

# Create Labels
# With the index argument, you can name your own labels.
print("=" *30)

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

# When you have created labels, you can access an item by referring to the label.
print("=" *30)

print(myvar["y"])

#Key/Value Objects as Series
# You can also use a key/value object, like a dictionary, when creating a Series.
print("=" *30)

calories = {"day1": 420, "day2": 380, "day3": 390} #Note: The keys of the dictionary become the labels.

myvar = pd.Series(calories)

print(myvar)

# To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.
print("=" *30)

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)