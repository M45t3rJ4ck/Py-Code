# K-Means clustering implementation
# Some hints on how to start have been added to this file.
# You will have to add more code that just the hints provided here for the full implementation.
# ====
import math
import pandas
import random as rand
import matplotlib.pyplot as plt


# Define a function that computes the distance between two data points
class Points:

    def __init__(self, x_, y_):
        self.coor_x = x_
        self.coor_y = y_

# ====


# Define a function that reads data in from the csv files  HINT: http://docs.python.org/2/library/csv.html
def file_read():
    data_places = []
    data = pandas.read_csv("data1953.csv")
    for line in data:
        places = Points(float(line[0]), float(line[1]))
        data_places.append(places)
    cluster = Clusters(data_places)
    cluster.print_clusters(Clusters.cluster)
# ====


# Write the initialisation procedure
class Clusters:
    def __init__(self, k_):
        self.k_ = k_
        self.means = []
        self.distance = {}
        self.cluster = {}
        self.count_ = []
        self.index = []
        self.min_ = self.distance[0]
        self.max_ = 0
        self.max_point = []

    def initial_means(self, points):
        point_ = rand.choice(points)
        self.cluster.setdefault(0, []).append(point_)
        points.remove(point_)
        for i in range(self.k_):
            point_ = self.next_point(i, points, self.cluster)
            self.cluster.setdefault(i, []).appened(point_)
            points.remove(point_)
        self.means = self.compute_means(self.cluster)

    def compute_means(self):
        for cluster in self.cluster.values():
            mean_point = Points(0.0, 0.0)
            cnt = 0.0
            for point in cluster:
                mean_point.coor_x += point.x
                mean_point.coor_y += point.y
                cnt += 1.0
            mean_point.coor_x = mean_point.coor_x / cnt
            mean_point.coor_y = mean_point.coor_y / cnt
            self.means.append(mean_point)
        return self.means

    def update_means(self, threshold):
        for i in range(len(self.means)):
            mean_1 = self.means[i]
            mean_2 = self.means[i]
            if math.sqrt(math.pow(mean_1.latit - mean_2.latit, 2.0) + math.pow(mean_1.longit - mean_2.longit, 2.0)) > threshold:
                return False
        return True

    def print_means(self):
        for point in self.means:
            print("point %f, %f" % (Points.coor_x, Points.coor_y))

    def get_point(self, points):
        for point in points:
            dist = []
            for mean in self.means:
                dist.append(math.sqrt(math.pow(point.x - mean.x, 2.0) + math.pow(point.y - mean.y, 2.0)))
            for num in self.distance:
                if num < self.min_:
                    self.min_ = num
                    self.index = self.count_
            self.count_ += 1
            self.cluster.setdefault(self.index, []).append(point)
        return self.cluster

    def next_point(self, max_point, points, cluster):
        for point_1 in points:
            for cluster in cluster.values():
                point_2 = cluster[0]
                if point_1 not in self.distance:
                    self.distance[point_1] = math.sqrt(math.pow(point_1.latit - point_2.latit, 2.0) + math.pow(point_1.longit - point_2.longit, 2.0))
                else:
                    self.distance[point_1] += math.sqrt(math.pow(point_1.latit - point_2.latit, 2.0) + math.pow(point_1.longit - point_2.longit, 2.0))
        for key, value in self.distance.item():
            if self.count_ == 0:
                self.max_ = value
                self.max_point = key
                self.count_ += 1
        return max_point

    def print_clusters(self, cluster):
        cluster_cnt = 1
        for cluster in cluster.values():
            print("Nodes in cluster #%d" % cluster_cnt)
            cluster_cnt += 1
            for Points in cluster:
                print("point %f, %f" % (Points.coor_x, Points.coor_y))
# ====


# Implement the k-means algorithm, using appropriate looping
def main():
    if len(file_read.data_places) < Clusters.k_:
        return -1
    Points.point_ = [point for point in file_read.data_places]
    cluster = Clusters.get_point(Clusters.point_)
    means = Clusters.compute_means(cluster)
    stop = Clusters.update_means(means, 0.01)
    if not stop:
        Clusters.means = []
        Clusters.means = means
    Clusters.cluster = cluster
    if plot_flag:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        markers = ['o', 'd', 'x', 'h', 'H', 7, 4, 5, 6, '8', 'p', ',', '+', '.', 's', '*', 3, 0, 1, 2]
        colors = ['r', 'k', 'b', [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
        cnt = 0
        for cluster in Clusters.cluster.values():
            x = []
            y = []
            for point in cluster:
                x.append(point.x)
                y.append(point.y)
            ax.scatter(x, y, s=60, c=colors[cnt], marker=markers[cnt])
            cnt += 1
        plt.show()
    return 0
# ====
# Print out the results


main()
