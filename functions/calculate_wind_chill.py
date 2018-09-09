#!/usr/bin/python3
import pathlib


"""
The following calculates 
"""


def TwC(T, V):
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
print("Wind chill {} ".format(wind_chill(0,-45,-5,0,20,2,p) )
