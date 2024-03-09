import pandas as pd

df = pd.read_csv('words.csv', index_col='Word')

df.head()

### Activities

##### How many elements does this dataframe have?

df.info()
df.shape

##### What is the value of the word `microspectrophotometries`?

df.loc["microspectrophotometries"]
df.loc["microspectrophotometries", "Value"]

##### What is the highest possible value of a word?

df.max()
df.describe()


##### Which of the following words have a Char Count of `7` and a Value of `87`?

df.loc[['glowing', 'superheterodyne', 'microbrew', 'pinfish', 'enfold']]


##### What is the highest possible length of a word?

df['Char Count'].max()
df.sort_values(by=["Value"], ascending=False)


##### What is the word with the value of `319`?

df.loc[df["Value"] == 319]

##### What is the most common value?

df["Value"].describe()
df["Value"].mode()

##### What is the shortest word with value `274`?

df.loc[df["Value"] == 274,'Char Count'].min()
df.loc[df["Value"] == 274].sort_values(by="Char Count")

##### Create a column `Ratio` which represents the 'Value Ratio' of a word

df["Ratio"] = df["Value"] / df["Char Count"]
df.head(10)

##### What is the maximum value of `Ratio`?

df["Ratio"].max()

##### What word is the one with the highest `Ratio`?

df.sort_values(by="Ratio", ascending= False).head

df.loc[df["Ratio"] ==df["Ratio"].max()]

##### How many words have a `Ratio` of `10`?

df.loc[df["Ratio"] == 10].shape
df.query("Ratio == 10").shape

##### What is the maximum `Value` of all the words with a `Ratio` of `10`?

df.loc[df['Ratio'] == 10, 'Value'].max()
df.query("Ratio == 10").max()

##### Of those words with a `Value` of `260`, what is the lowest `Char Count` found?

df.loc[df['Value'] == 260, 'Char Count'].min()
df.query("Value == 260").min()

##### Find all the words with Char Count > avg char count

mean_char_count = df['Char Count'].mean()
mean_char_count

df.query("`Char Count` > @mean_char_count")

##### Based on the previous task, what word is it?

df.loc[(df['Value'] == 260) & (df['Char Count'] == 17)]


