import Scraper
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
from datetime import datetime
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt


# This function can likely be converted into a one-liner
def AddDays(x, days):
    new_x = list()
    for day in range(days+1):
        new_x.append(x[len(x)-1] + pd.to_timedelta(day, unit='D')) 
    return new_x

# Collect data
scraper = Scraper.Scraper()
data = scraper.ScrapeData()
x = data[0]
y = data[1]

# ARIMA Model Settings
settings = (5,1,0)
percentage_training = 0.40

#Set up forecasting period
forecast_days = 300
# print(x[len(x)-4:len(x)-1])
x_forecast = AddDays(x.copy(), forecast_days) # This extends x by forecast_days



# Split data into training and test sets
size = int(len(y) * percentage_training) # size of the training set - first part of y. Also need to segement X the same way
print(size)
train_x, test_x = x[0:size], x[size:len(x)] # Note that the training set ends before the end of the whole x series for convenience
train_y, test_y = y[0:size], y[size:len(y)]

# Training data for the beginning of the model
history = [y for y in train_y]
predictions = list()

for t in range(len(test_y)):
    model = ARIMA(history, order=settings)
    model_fit = model.fit()
    output = model_fit.forecast()
    yhat = output[0]
    predictions.append(yhat)
    obs = test_y[t]
    history.append(obs)
    print('Predicted Cases=%f, Expected Cases=%f' % (yhat, obs))


model_fit = model.fit()
future_predictions = model_fit.predict(len(y), len(y) + forecast_days)

# evaluate forecasts
rmse = sqrt(mean_squared_error(test_y, predictions))
print('Test RMSE: %.3f' % rmse)

plt.plot(x, y, color="yellow", label = "full set")
plt.plot(test_x, predictions, "--", color='red', label="Prediction")
plt.plot(x_forecast, future_predictions, color='green', label="Future Prediction")

plt.title("Future Prediction")
plt.legend(loc="lower right")
plt.show()

