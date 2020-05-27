import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets, svm
import numpy as np

################################################################################

# Import Iris data set
# Select two dimensions that give convenient data
iris = datasets.load_iris()
X = iris.data[:, [1, 3]]
y = iris.target

################################################################################

# Plot raw data
fig, axes = plt.subplots(nrows=1, ncols=1)
axes.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor='k')
axes.set_xlabel('Sepal length')
axes.set_ylabel('Sepal width')
axes.set_xticks(())
axes.set_yticks(())
axes.set_title('Raw data')

################################################################################

# Convert to two two classes
newy = []
for t in y:
    if t==0: newy.append(0)
    else: newy.append(1)
y = newy

# Plot two class data
fig, axes = plt.subplots(nrows=1, ncols=1)
axes.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor='k')
axes.set_xlabel('Sepal length')
axes.set_ylabel('Sepal width')
axes.set_xticks(())
axes.set_yticks(())
axes.set_title('Two-class problem')

################################################################################

# Run SVM on two class data
#clf = svm.SVC() # non linear kernel!
clf = svm.SVC(kernel='linear', C=1000)
clf.fit(X, y)

# Plot two class data with SVM result
fig, axes = plt.subplots(nrows=1, ncols=1)
axes.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor='k')
axes.set_xlabel('Sepal length')
axes.set_ylabel('Sepal width')
axes.set_xticks(())
axes.set_yticks(())
axes.set_title('Two-class problem - Linear SVM')

# plot the decision function
xlim = axes.get_xlim()
ylim = axes.get_ylim()

# create grid to evaluate model
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

# plot decision boundary and margins
axes.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
           linestyles=['--', '-', '--'])
# plot support vectors
axes.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100,
           linewidth=1, facecolors='none', edgecolors='k')

################################################################################

plt.show()
