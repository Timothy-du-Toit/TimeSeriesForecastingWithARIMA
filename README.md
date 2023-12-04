# Forecasting COVID-19 Cases using AIRMA models in Python

I enjoyed this little project - tackling it on Saturday afternoon. I had worked with the same ARIMA library a while ago for a personal project and it was great to hop back in! 

# A Note on Test Data
It appears as though new SA  COVID-19 cases are no longer being recorded on [WorldOMeters](https://www.worldometers.info/coronavirus/country/south-africa/). 
As such, for the past while, the daily increase in the number of cases has been set to 0. You can exclude this when running my script by modifying the `exclude_days` value in `main.py`. I recommend `exclude_days = 400` to better demonstrate the predictive capabilities of this model

# Getting Started
## Required Libraries

- matplotlib.pyplot
- pandas
- BeautifulSoup (pip install bs4)
- datetime
- statsmodels.tsa.arima.model
- sklearn.metrics

## Running the Script
Open the folder location of the script in your terminal and simply run the below command:
`python main.py`

## Output
The requested output .csv and .png will be placed into the parent folder. 
1. all_data_graph.png contains the original data (train + test), and the 7 days prediction
2. prediction_graph.png contains just the 7 days prediction
3. output_prediction.csv contains the raw 7 day prediction data

# Cheers
Feel free to reach out to me at:
1. LinkedIn: www.linkedin.com/in/timothy-dt
