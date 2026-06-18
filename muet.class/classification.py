from sklearn.tree import DecisionTreeClassifier
import numpy as np

X=np.array([1,2,3,4,5]).reshape(-1,1)
Y=np.array([
    "fail", "fail", "fail", "pass", "pass"
])

model = DecisionTreeClassifier()
model.fit(X,Y)
print(model.predict([[6]]))