import os
import pandas as pd
from neuralprophet import NeuralProphet

import plotly


# Full file path to your CSV file
file_path = "D:/Libraries/Documents/Python Projects/Neuralprophet/ada_usdt_15m_extended.csv"

# Load the data, ensuring to parse the timestamp correctly
df = pd.read_csv(file_path, parse_dates=['timestamp'])

# Ensure your DataFrame has the columns 'ds' for date and 'y' for the value to predict
df['ds'] = df['timestamp']
df['y'] = df['close']  # You can use 'open', 'low', 'high', or 'close'

# Keep only the necessary columns for NeuralProphet
df = df[['ds', 'y']]

# Initialize and fit the NeuralProphet model
model = NeuralProphet()
model.fit(df, freq='15min')

# Make predictions
future = model.make_future_dataframe(df, periods=96)  # Predict for next 24 hours (96 * 15min intervals)
forecast = model.predict(future)

# Plot the results
model.plot(forecast)
model.plot_components(forecast)
