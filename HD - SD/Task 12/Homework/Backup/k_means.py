# K-Means clustering implementation
# Some hints on how to start have been added to this file.
# You will have to add more code that just the hints provided here for the full implementation.
# ====
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np


# Define a function that computes the distance between two data points
# ====
class Point:

    def __init__(self, point_1, point_2):
        self.point1 = point_1
        self.point2 = point_2

    def distance(self):
        dist = math.sqrt(math.pow(self.point_1[0] - self.point_2[0], 2.0) + math.pow(self.point_1[0] - self.point_2[0], 2.0))
        return dist


# Define a function that reads data in from the csv files
def csv_read():
    df = pd.read_csv("data1953.csv")
    print(df)
    df2 = pd.read_csv("data2008.csv")
    print(df2)
    df3 = pd.read_csv("dataBoth.csv")
    print(df3)
    classes_L = df["LifeExpectancy"]
    classes_B = df["BirthRate"]
    return df, classes_L, classes_B
# ====

# Write the initialisation procedure

# ====


# Implement the k-means algorithm, using appropriate looping
df, classes_L, classes_B = csv_read()
df = df.drop(['Countries'], axis=1)
data = df.values.tolist()
data = np.array(data)
train_data = data[:147]
test_data = data[147:]

# ====
# Print out the results
plt.figure(1, figsize=(9, 3))
plt.subplot(131)
plt.bar(data)
plt.show()
