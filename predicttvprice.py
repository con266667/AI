from sklearn import tree

#features = [quality, size]
features = [[1080, 43], [720, 32], [1080, 49], [3840, 55], [3840, 42], [3840, 49]]

#prices
labels = [300, 150, 400, 500, 450, 550]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
quality = input("What's the quality of the tv?")
size = input("What's the size of the tv?")
print(clf.predict([[quality, size]]))