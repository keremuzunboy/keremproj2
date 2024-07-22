import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Define the ticker
ticker = "TSPOR.IS"  # Example ticker

# Download data
data = yf.download(ticker, start="2020-01-01", end="2024-01-01")

# Prepare data
data['Prediction'] = data['Close'].shift(-1)
data = data.dropna()

X = data[['Open', 'High', 'Low', 'Close', 'Volume']]
y = data['Prediction']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
prediction = model.predict(X_test)

# Visualize results
plt.figure(figsize=(16,8))
plt.plot(y_test.values, label='Actual')
plt.plot(prediction, label='Predicted')
plt.legend()
plt.show()