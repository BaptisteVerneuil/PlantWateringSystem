from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_moisture(moisture_past, date_moisture_past, weights, precipitation_forecast):

    # The unweighted model
    regr = LinearRegression()
    date_moisture_past = np.array(date_moisture_past).reshape(-1, 1)
    moisture_past = np.array(moisture_past).reshape(-1, 1)

    regr.fit(date_moisture_past, moisture_past, weights)
    return regr

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    date_moisture_past=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5]
    moisture_past=[40, 37, 27, 22, 20, 12, 17, 14, 16, 14, 12, 9]
    
    weights = [80*0.8**(len(moisture_past) - i) for i in range(len(moisture_past))]

    plt.scatter(date_moisture_past, moisture_past, s=weights, c='grey', edgecolor='black')

    precipitation_forecast = [0 for i in range(24)]

    regr = forecast_moisture(moisture_past, date_moisture_past, weights, precipitation_forecast)
    plt.plot(date_moisture_past, regr.predict(np.array(date_moisture_past).reshape(-1, 1)), color='blue', linewidth=3, label='Unweighted model')
    plt.show()

    
