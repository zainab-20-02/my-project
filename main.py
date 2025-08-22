#py -3.13 -m pip install pandas
# pip install pandas
import pandas as pd

# Using forward slashes works on all systems and is easier to read.
# Using .head() is good practice to preview the data without printing the entire file.
df = pd.read_csv("c:/users/pc/Documents/movie dataset tmdb.csv")
print(df.head())

print(df.columns)
print(df.shape)