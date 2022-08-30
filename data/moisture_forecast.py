import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

"""
Functions for weighted linear regression
"""

def multiply_matrix(x, y):
    return [x[i] * y[i] for i in range(len(x))]

def estimate_coef(x, y):
    """
    Return the coefficients of the linear regression fitting the points listed int he lists x and y
    Inspired from https://github.com/OpenGenus/quark/blob/master/code/code/artificial_intelligence/src/Linear_Regression/linear_regression.py
    ---------------------
    parameters:
    x: list of floats
        list of the points x-axis
    y: list of floats
        list of the points y-axis
    """
    # number of observations/points
    n = len(x)
  
    # mean of x and y vector
    m_x = sum(x) / len(x)
    m_y = sum(y) / len(y)
  
    # calculating cross-deviation and deviation about x
    SS_xy = sum(multiply_matrix(y, x)) - n*m_y*m_x
    SS_xx = sum(multiply_matrix(x, x)) - n*m_x*m_x
  
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
  
    return (b_0, b_1)

def update_x_y_weight(x, y, w):
    """
    Function to convert a weighted linear regression problem into a classical linear regression problem
    Return the new lists of describing the points taking into account the weight of each point
    ---------------------
    parameters:
    x: list of floats
        list of the points x-axis
    y: list of floats
        list of the points y-axis
    w: list of floats
        list of the points weight
    """
    # turning weights into integers between 0 and 1000
    max_w = max(w)
    w = [int((w[i]*1000)/max_w) for i in range(len(w))]

    # We add in the new list new_x the x[i] value w[i] times (resp. new_y and y[i])
    new_x, new_y = [], []
    for i in range(len(x)):
        for j in range(w[i]):
            new_x.append(x[i])
            new_y.append(y[i])
    return new_x, new_y

def weighted_linear_regression(x, y, w):
    return estimate_coef(*update_x_y_weight(x, y, w))

"""
Functions for forecasting the soil moisture
"""

def forecast_moisture(moisture_past, date_moisture_past, weights, precipitation_forecast, dates_forecast, plot=False):
    """
    Function for forecasting the soil moisture, taken into account the precipitation forecast, using a weighted linear regression
    Return the list of the future moisture, as well as the coefficient of the weitghed linear regression
    ---------------------
    parameters:
    moisture_past: list of floats
        list of the moisture measurements
    date_moisture_past: list of floats
        list of the dates asociated with each moisture measurement
    weights: list of floats
        list of the points weight
    precipitation_forecast: list of floats
        list of precipitation forecast
    dates_forecast: list of floats
        list of the dates of the precipitation forecast
    plot: boolean
        Boolean set to True if we want to plot the linear regression
    """

    b = weighted_linear_regression(date_moisture_past, moisture_past, weights)

    # Used for plotting the weighted regression
    if plot==True : 
        y_pred = [b[1]*date_moisture_past[i]+b[0] for i in range(len(date_moisture_past))]
        import matplotlib.pyplot as plt
        plt.scatter(date_moisture_past, moisture_past, s=weights, c='grey', edgecolor='black')
        plt.plot(date_moisture_past, y_pred, color='blue', linewidth=3, label='Weighted model')
        plt.legend()
        plt.show()

    # returning predicted moisture
    future_moisture = [b[1]*dates_forecast[i]+b[0] for i in range(len(dates_forecast))]

    # Adding the precipitation
    for i,p in enumerate(precipitation_forecast):
        if p!=0:
            for j in range(i, len(future_moisture)):
                future_moisture[j]+=p*config.area_plant*config.conversion_moisture_volume

    return future_moisture, b

if __name__ == "__main__":

    # For testing purposes

    # Creating fake values
    date_moisture_past=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5]
    moisture_past=[80, 74, 54, 44, 40, 24, 34, 28, 32, 28, 24, 18]
    weights = [80*0.8**(len(moisture_past) - i) for i in range(len(moisture_past))]
    precipitation_forecast = [0 for i in range(24)]

    # Forecting the next values
    _,b = forecast_moisture(moisture_past, date_moisture_past, weights, precipitation_forecast, date_moisture_past, plot=True)

    arr = date_moisture_past + [7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5]
    predict = [b[1]*arr[i]+b[0] for i in range(len(arr))]
    for i in range(4):
        predict[-i-1]+=30
    
    # Plotting the results
    import matplotlib.pyplot as plt
    plt.scatter(date_moisture_past, moisture_past, s=weights, c='grey', edgecolor='black')
    plt.plot(arr, predict, color='blue', linewidth=3, label='Moisture forecast')
    plt.legend()
    plt.show()

    
