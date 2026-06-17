from sklearn.linear_model import LinearRegression
import numpy as np

X=np.array([1,2,3,4,5]).reshape(-1,1)
Y=np.array([20,40,60,80,100])

model=LinearRegression()

model.fit(X,Y)

print(model.predict([[6]]))
