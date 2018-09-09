#!/usr/bin/python3


def convert_temperature(*, f_temp=None, c_temp=Non):
    if c_temp is None:
        return {'f_temp': f_temp, 'c_temp': 5*(f_temp-32)/9}
    if f_temp is None:
        return {'f_temp': 32+9*c_temp/5, 'c_temp': c_temp}
    else:
        raise Exception("Niether Fahrenheit nor Celcius temprature was provided")



