# Define a function that reads data in from the csv files  HINT: http://docs.python.org/2/library/csv.html
def ReadCSV():
    # data is read from CSV using pandas csv library
    import pandas
    # df = pandas.read_csv('data1953.csv')
    # df = pandas.read_csv('data2008.csv')
    df = pandas.read_csv('dataBoth.csv')
    # print(df)
    classes = df['LifeExpectancy']
    return df, classes


# ====
# Write the initialisation procedure
# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# ====
# Implement the k-means algorithm, using appropriate looping
df, classes = ReadCSV()
# Drop the other coloumn Countries values from data
df = df.drop(['Countries'], axis=1)

# Convert dataframe into list and then into a numpy array
data = df.values.tolist()
data = np.array(data)
# print(data)

# First 147 points (75% of set) are used for training and the rest is used for testing
train_data = data[:147]
test_data = data[147:]
