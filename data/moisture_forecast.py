from sklearn.linear_model import LinearRegression
import numpy as np
import config

def forecast_moisture(moisture_past, date_moisture_past, weights, precipitation_forecast, dates_forecast):

    # Weighted model
    regr = LinearRegression()
    date_moisture_past = np.array(date_moisture_past).reshape(-1, 1)
    moisture_past = np.array(moisture_past).reshape(-1, 1)
    regr.fit(date_moisture_past, moisture_past, weights)

    """
    import matplotlib.pyplot as plt
    plt.scatter(date_moisture_past, moisture_past, s=weights, c='grey', edgecolor='black')
    plt.plot(date_moisture_past, regr.predict(np.array(date_moisture_past).reshape(-1, 1)), color='blue', linewidth=3, label='Unweighted model')
    plt.show()
    """

    # returning predicted moisture
    future_moisture = regr.predict(np.array(dates_forecast).reshape(-1, 1))

    # Adding the precipitation
    for i,p in enumerate(precipitation_forecast):
        if p!=0:
            for j in range(i, len(future_moisture)):
                future_moisture[j]+=p*(10**(-3))*config.area_plant*config.conversion_moisture_volume

    return future_moisture, regr

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    date_moisture_past=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5]
    moisture_past=[40, 37, 27, 22, 20, 12, 17, 14, 16, 14, 12, 9]
    
    weights = [80*0.8**(len(moisture_past) - i) for i in range(len(moisture_past))]

    plt.scatter(date_moisture_past, moisture_past, s=weights, c='grey', edgecolor='black')

    precipitation_forecast = [0 for i in range(24)]

    _,regr = forecast_moisture(moisture_past, date_moisture_past, weights, precipitation_forecast)

    plt.plot(date_moisture_past, regr.predict(np.array(date_moisture_past).reshape(-1, 1)), color='blue', linewidth=3, label='Unweighted model')
    plt.show()

    
