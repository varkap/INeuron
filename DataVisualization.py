import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn import datasets
import pandas as pd
iris = datasets.load_iris() 
X = iris.data 
target = iris.target 
names = iris.target_names
labels = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']
df = pd.DataFrame(data=X, columns=labels)
ax = plt.axes(projection='3d')
x = df['Sepal Length']
y = df['Sepal Width']
z = df['Petal Length']
w = df['Petal Width']
plot = ax.scatter3D(x,y,z,cmap=w)