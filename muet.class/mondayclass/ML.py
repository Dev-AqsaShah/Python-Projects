from sklearn.linear_model import LinearRegression


X = [[1000], [8900], [550]]
Y = [1000, 1210, 1500]

model = LinearRegression()
model.fit(X,Y)
price = model.predict([[1400]])
print(price)
