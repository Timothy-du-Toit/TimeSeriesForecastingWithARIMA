import scraper
import helper
import matplotlib.pyplot as plt 
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt
import warnings
import os


#Application Set-Up
exclude_days = 0
silent_run = True

if(silent_run):
    warnings.filterwarnings("ignore")

# Collect data
data = scraper.scrape_data()
x = data[0][0: len(data[0]) - exclude_days]
y = data[1][0: len(data[1]) - exclude_days]

# ARIMA Model Settings
settings = (3,1,0)
percentage_training = 0.50

#Set up forecasting period
forecast_days = 7
x_forecast = helper.add_days(x.copy(), forecast_days) # This extends x by forecast_days

# Split data into training and test sets
size = int(len(y) * percentage_training)
print(f"Traininig set consists of {size} data points")
train_x, test_x = x[0:size], x[size:len(x)]
train_y, test_y = y[0:size], y[size:len(y)]

# Training data for the beginning of the model
history = [y for y in train_y]
predictions = list()

print("Developing model...")
for t in range(len(test_y)):
    model = ARIMA(history, order=settings)
    model_fit = model.fit()
    output = model_fit.forecast()
    yhat = output[0]
    predictions.append(yhat)
    obs = test_y[t]
    history.append(obs)
    if(silent_run != True):
        print('Predicted Cases=%f, Expected Cases=%f' % (yhat, obs))
print("Model development completed")

model_fit = model.fit()
future_predictions = model_fit.predict(len(y), len(y) + forecast_days - 1)

# evaluate forecasts
rmse = sqrt(mean_squared_error(test_y, predictions))
print('Test RMSE: %.3f' % rmse)

# Plot the various graphs
plt.plot(x_forecast, future_predictions, color='green', label="Future Prediction")
plt.title("Prediciton of African Covid Cases")
plt.legend(loc="lower right")

# Save the graphs
output_graph = os.path.join("prediction_graph.png")
plt.savefig(output_graph)

plt.plot(x, y, color="yellow", label = "Full Dataset")
plt.plot(test_x, predictions, "--", color='red', label="Prediction with Dataset")
output_graph = os.path.join("all_data_graph.png")
plt.savefig(output_graph)
plt.legend(loc="lower right")

# Save the future prediction data
dataset = {}
dataset = {"date": x_forecast, "new_cases": future_predictions}
dailyCases = pd.DataFrame(data=dataset)
output_file = os.path.join("output_prediction.csv")
dailyCases.to_csv(output_file, index=False)	

plt.show()