import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def get_crypto_data(symbol, start_date, end_date):
    ticker = yf.Ticker(f"{symbol}-USD")
    df = ticker.history(start=start_date, end=end_date, interval="1h")
    return df

def add_technical_indicators(df):
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['RSI'] = calculate_rsi(df['Close'], 14)
    df['MACD'], df['Signal'] = calculate_macd(df['Close'])
    df['Volatility'] = df['Close'].pct_change().rolling(window=20).std()
    return df

def calculate_rsi(prices, period=14):
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def calculate_macd(prices, slow=26, fast=12, smooth=9):
    exp1 = prices.ewm(span=fast, adjust=False).mean()
    exp2 = prices.ewm(span=slow, adjust=False).mean()
    macd = exp1 - exp2
    signal = macd.ewm(span=smooth, adjust=False).mean()
    return macd, signal

def prepare_data(df):
    df = df.dropna()
    df['Target'] = df['Close'].shift(-1)
    df = df.dropna()
    
    features = ['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_20', 'SMA_50', 'RSI', 'MACD', 'Signal', 'Volatility']
    X = df[features]
    y = df['Target']
    
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    return model, scaler

def evaluate_model(model, X_test, y_test, scaler):
    X_test_scaled = scaler.transform(X_test)
    predictions = model.predict(X_test_scaled)
    
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R-squared Score: {r2:.2f}")
    
    return predictions

def plot_results(df, predictions):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index[-len(predictions):], df['Close'][-len(predictions):], label='Gerçek Fiyat')
    plt.plot(df.index[-len(predictions):], predictions, label='Tahmin')
    plt.title('Kripto Para Tahmin Sonuçları')
    plt.xlabel('Tarih')
    plt.ylabel('Fiyat (USD)')
    plt.legend()
    plt.show()

def predict_next_period(model, scaler, last_data):
    last_data_scaled = scaler.transform(last_data.reshape(1, -1))
    prediction = model.predict(last_data_scaled)
    return prediction[0]

# Ana program
if __name__ == "__main__":
    symbol = "MOVR"  # Bitcoin örneği
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    
    df = get_crypto_data(symbol, start_date, end_date)
    df = add_technical_indicators(df)
    
    X_train, X_test, y_train, y_test = prepare_data(df)
    
    model, scaler = train_model(X_train, y_train)
    predictions = evaluate_model(model, X_test, y_test, scaler)
    
    plot_results(df, predictions)
    
    last_data = df.iloc[-1][['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_20', 'SMA_50', 'RSI', 'MACD', 'Signal', 'Volatility']].values
    next_period_prediction = predict_next_period(model, scaler, last_data)
    print(f"Bir sonraki periyot için tahmin edilen {symbol} fiyatı: {next_period_prediction:.2f} USD")