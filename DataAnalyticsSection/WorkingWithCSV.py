import os
import pandas as pd

# creates dataframe from csv
df = pd.read_csv('DataAnalyticsSection/Netflix_Dataset.csv') 
# df.to_csv('scary_pets.csv') will change df into csv, index=False will remove index
# na_rep='**empty**' will replace empty values
print(df)