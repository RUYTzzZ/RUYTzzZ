# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

"""
Please note, this code is only for python 3+. If you are using python 2+, please modify the code accordingly.
"""


from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
iris = datasets.load_iris()

X = iris.data
y = iris.target

##print(iris_X[:2, :])
##print(iris_y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

##print(y_train)

model =KNeighborsClassifier()
model.fit(X_train, y_train)


print(model.predict(X_test))
print(y_test)

predict_data = model.predict(X)
accuracy =np.mean(predict_data==y)
print(accuracy)

