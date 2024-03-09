import pandas as pd
# to see the version of the pandas
print(pd.__version__)

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)


# A Pandas Series is like a column in a table.
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

# Labels
# If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
# This label can be used to access a specified value
print(myvar[0]) #Return the first value of the Series:
