#!/usr/bin/python3

"""
The following calculates wind chill temparature.

For more information on the formula used below refer to:
https://en.wikipedia.org/wiki/Wind_chill#North_American_and_United_Kingdom_wind_chill_index

"""

import pathlib
import csv

def TwC(T, V):
    """Computes the wind chill temperature
    The wind-chill, :math:`T_{wc}`, is based on
    air temperature, T, and wind speed, V.

    :param T: Temperature in °C
    :param V: Wind Speed in kph
    :returns: Wind-Chill temperature in °C
    :raises ValueError: for wind speed under 4.8kph or Temperature above 10°C

    >>> round(TwC(-10, 25), 1)
    """
    if V < 4.8 or T > 10.0:
        raise ValueError("V must be over 4.8kph, Temperature must be below 10°C")
    return 13.12 + 0.6215*T - 11.37*V**0.16 + 0.3965*T*V**0.16

def wind_chill(start_T, stop_T, step_T, start_V, stop_V, step_V, path):
    """ Wind Chill Table."""
    with path.open('w', newline='') as target:
        writer = csv.writer(target)
        heading = [None] + list(range(start_T, stop_T, step_T))
        writer.writerow(heading)
        for V in range(start_V, stop_V, step_V):
            row = [V] + [TwC(T, V) for T in range(start_T, stop_T, step_T)]
            writer.writerow(row)


p=pathlib.Path("wc.csv")
print("Wind chill {} ".format(wind_chill(10,12,1,50,10,1,p) ))
