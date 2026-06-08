import numpy as np 
from sklearn.linear_model import LinearRegression 
x_raw = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
y_raw = [40, 43, 46, 49, 52, 55, 58, 61, 64, 67]

x = np.array(x_raw).reshape(-1, 1)
y = np.array(y_raw)

model = LinearRegression()

model.fit(x,y)
y_pred = model.predict(x)

new_ad_spend = np.array([[20]])
predicted_sales = model.predict(new_ad_spend)

#  print(f"\nPredicted sales for $20k ad spend: {predicted_sales[0]:.2f}")


