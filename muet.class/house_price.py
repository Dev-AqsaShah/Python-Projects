from sklearn.linear_model import LinearRegression
import numpy as np

# row = [floor, square(area)]
X = np.array([
    [1, 120],
    [2, 240],
    [3, 360]
])

# Target = price 
Y = np.array([10000000, 20000000, 30000000])

model = LinearRegression()
model.fit(X, Y)

# floor = 4 , area = 480 , house price?
predicted = model.predict([[4, 480]])
print("Predicted price:", predicted)