import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import mplfinance as mpf
from datetime import datetime, timedelta
import ta

def get_crypto_data(symbol, start_date, end_date):
    ticker = yf.Ticker(f"{symbol}-USD")
    df = ticker.history(start=start_date, end=end_date, interval="1h")
    return df

def add_technical_indicators(df):
    df['SMA_20'] = ta.trend.sma_indicator(df['Close'], window=20)
    df['SMA_50'] = ta.trend.sma_indicator(df['Close'], window=50)
    df['RSI'] = ta.momentum.rsi(df['Close'], window=14)
    df['MACD'] = ta.trend.macd_diff(df['Close'])
    df['BB_up'], df['BB_mid'], df['BB_low'] = ta.volatility.bollinger_hband_indicator(df['Close']), ta.volatility.bollinger_mavg(df['Close']), ta.volatility.bollinger_lband_indicator(df['Close'])
    df['ATR'] = ta.volatility.average_true_range(df['High'], df['Low'], df['Close'])
    df['OBV'] = ta.volume.on_balance_volume(df['Close'], df['Volume'])
    return df

def prepare_data(df):
    df = df.dropna()
    df['Target'] = df['Close'].shift(-1)
    df = df.dropna()
    
    features = ['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_20', 'SMA_50', 'RSI', 'MACD', 'BB_up', 'BB_low', 'ATR', 'OBV']
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
    # Mum grafiği için veri hazırlığı
    df_plot = df[-len(predictions):].copy()
    df_plot['Predictions'] = predictions

    # Özel stil tanımlama
    mc = mpf.make_marketcolors(up='g', down='r', inherit=True)
    s = mpf.make_mpf_style(marketcolors=mc, gridstyle=':', y_on_right=False)

    # Ek grafikler
    ap = [
        mpf.make_addplot(df_plot['SMA_20'], color='blue', width=0.7),
        mpf.make_addplot(df_plot['SMA_50'], color='red', width=0.7),
        mpf.make_addplot(df_plot['Predictions'], type='scatter', markersize=3, color='fuchsia'),
        mpf.make_addplot(df_plot['RSI'], panel=1, color='purple', ylabel='RSI'),
        mpf.make_addplot(df_plot['MACD'], panel=2, color='green', ylabel='MACD'),
        mpf.make_addplot(df_plot['Volume'], panel=3, type='bar', ylabel='Volume')
    ]

    # Grafiği çizme
    mpf.plot(df_plot, type='candle', style=s, addplot=ap, volume=False, 
             title=f'Kripto Para Analizi ve Tahminleri\nMSE: {mse:.2f}, R2: {r2:.2f}',
             figsize=(12, 10), panel_ratios=(6,2,2,2))

def predict_next_period(model, scaler, last_data):
    last_data_scaled = scaler.transform(last_data.reshape(1, -1))
    prediction = model.predict(last_data_scaled)
    return prediction[0]

# Ana program
if __name__ == "__main__":
    symbol = "BTC"  # Bitcoin örneği
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    
    df = get_crypto_data(symbol, start_date, end_date)
    df = add_technical_indicators(df)
    
    X_train, X_test, y_train, y_test = prepare_data(df)
    
    model, scaler = train_model(X_train, y_train)
    predictions = evaluate_model(model, X_test, y_test, scaler)
    
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    plot_results(df, predictions)
    
    last_data = df.iloc[-1][['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_20', 'SMA_50', 'RSI', 'MACD', 'BB_up', 'BB_low', 'ATR', 'OBV']].values
    next_period_prediction = predict_next_period(model, scaler, last_data)
    print(f"Bir sonraki periyot için tahmin edilen {symbol} fiyatı: {next_period_prediction:.2f} USD")