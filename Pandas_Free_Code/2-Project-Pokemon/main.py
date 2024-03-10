## Project: Querying and Filtering Pokemon data

# This project will help you practice your pandas querying and filtering skills. Let's begin!


### Task 0 - Setup

# There isn't much to do here, we'll provide the required imports and the read the pokemon CSV we'll be working with.

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("pokemon.csv")

df.head()

df.info()

df.describe()

#### Distribution of Pokemon Types:

df['Type 1'].value_counts().plot(kind='pie', autopct='%1.1f%%', cmap='tab20c', figsize=(10, 8))

#### Distribution of Pokemon Totals:

df['Total'].plot(kind='hist', figsize=(10, 8))

df['Total'].plot(kind='box', vert=False, figsize=(10, 5))

#### Distribution of Legendary Pokemons:

df['Legendary'].value_counts().plot(kind='pie', autopct='%1.1f%%', cmap='Set3', figsize=(10, 8))

### Basic filtering

# Let's start with a few simple activities regarding filtering.

##### 1. How many Pokemons exist with an `Attack` value greater than 150?

# Doing a little bit of visual exploration, we can have a sense of the most "powerful" pokemons (defined by their "Attack" feature). A boxplot is a great way to visualize this:

sns.boxplot(data=df, x='Attack')

df.loc[df["Attack"] > 150]

(df["Attack"] > 150).sum()

df.query("Attack > 150")

##### 2. Select all pokemons with a Speed of `10` or less

sns.boxplot(data=df, x='Speed')

df.loc[df["Speed"]<= 10]

(df["Speed"] <= 10).sum()

slow_pokemons_df = df.loc[df["Speed"]<= 10]

##### 3. How many Pokemons have a `Sp. Def` value of 25 or less?

(df["Sp. Def"] <= 25).sum()

##### 4. Select all the Legendary pokemons

df.info()

df.loc[df["Legendary"]]

legendary_df = df.loc[df["Legendary"] == True]

##### 5. Find the outlier

# Find the pokemon that is clearly an outlier in terms of Attack / Defense:

ax = sns.scatterplot(data=df, x="Defense", y="Attack")
ax.annotate(
    "Who's this guy?", xy=(228, 10), xytext=(150, 10), color='red',
    arrowprops=dict(arrowstyle="->", color='red')
)

df.loc[df["Defense"] > 200]

### Advanced selection

# Now let's use boolean operators to create more advanced expressions

##### 6. How many Fire-Flying Pokemons are there?

(df["Type 1"] == "Fire").sum()

(df["Type 2"] == "Flying").sum()

((df["Type 1"] == "Fire") & (df["Type 2"] == "Flying")).sum()

df.loc[(df["Type 1"] == "Fire") & (df["Type 2"] == "Flying")]

df.query("`Type 1` == 'Fire' and `Type 2` == 'Flying'")

##### 7. How many 'Poison' pokemons are across both types?

df.query("`Type 1` == 'Poison' or `Type 2` == 'Poison'")

((df["Type 1"] == "Poison") | (df["Type 2"] == "Poison")).sum()

df.loc[(df["Type 1"] == "Poison") | (df["Type 2"] == "Poison")]

##### 8. Name the pokemon of `Type 1` *Ice* which has the strongest defense?

df.loc[df["Type 1"] == "Ice", "Defense"].max()

df.loc[
    (df["Type 1"] == "Ice") &
    (df["Defense"] == df.loc[df["Type 1"] == "Ice", "Defense"].max())
].head()

df.loc[
    (df["Type 1"] == "Ice") &
    (df["Defense"] == df.loc[df["Type 1"] == "Ice", "Defense"].max())
].iloc[0,1]

df.loc[df["Type 1"] == "Ice"].sort_values("Defense", ascending = False).head()

##### 9. What's the most common type of Legendary Pokemons?

df.loc[df["Legendary"], "Type 1"].value_counts().plot(kind="bar")

##### 10. What's the most powerful pokemon from the first 3 generations, of type water?

df["Generation"].isin([1,2,3]).sum()

df.loc[

    df['Generation'].isin((1, 2, 3)) &
    (df['Type 1'] == 'Water')

].sort_values(by='Total', ascending=False).head()


##### 11. What's the most powerful Dragon from the last two generations?

df.loc[
    ((df["Type 1"] == "Dragon") |
    (df["Type 2"] == "Dragon")) &
    (df["Generation"].isin({5, 6}))
].sort_values(by='Total', ascending=False).head()

##### 12. Select most powerful Fire-type pokemons

df.loc[
    (df["Type 1"] == "Fire") &
    (df["Attack"] > 100)

].sort_values(by='Total', ascending=False).head()

# Try your code here
powerful_fire_df = df.loc[
    (df["Type 1"] == "Fire") &
    (df["Attack"] > 100)

]

##### 13. Select all Water-type, Flying-type pokemons

water_flying_df = df.loc[
    (df["Type 1"] == "Water") &
    (df["Type 2"] == "Flying")
]

##### 14. Select specific columns of Legendary pokemons of type Fire

# Try your code here
legendary_fire_df = df.loc[
    (
        (df["Type 1"] == "Fire")&
        (df["Legendary"])
    ),
    ["Name", "Attack", "Generation"]
]

##### 15. Select Slow and Fast pokemons

# This is the distribution of speed of the pokemons. The red lines indicate those bottom 5% and top 5% pokemons by speed:

ax = df['Speed'].plot(kind='hist', figsize=(10, 5), bins=100)
ax.axvline(df['Speed'].quantile(.05), color='red')
ax.axvline(df['Speed'].quantile(.95), color='red')

botton5 = df['Speed'].quantile(.05)
top5 = df['Speed'].quantile(.95)

botton5, top5

df.loc[(df["Speed"] < botton5) | (df["Speed"] > top5)]

# Try your code here
slow_fast_df = df.loc[(df["Speed"] < botton5) | (df["Speed"] > top5)]

##### 16. Find the Ultra Powerful Legendary Pokemon

fig, ax = plt.subplots(figsize=(14, 7))
sns.scatterplot(data=df, x="Defense", y="Attack", hue='Legendary', ax=ax)
ax.annotate(
    "Who's this guy?", xy=(140, 150), xytext=(160, 150), color='red', arrowprops=dict(arrowstyle="->", color='red')
)

# Try your code here

### The End!