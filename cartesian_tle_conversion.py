import csv
import numpy as np
from sgp4.api import Satrec
import juliandate as jd
import satkit
import time

tle = open(r"C:\Users\xa360\Documents\div\NUSTAR.txt")
unpack_tle = tle.readlines()
l1 = unpack_tle[1]
l2 = unpack_tle[2]

sc = Satrec.twoline2rv(l1 , l2)

def interval(yr0 , month0 , day0 , hr0 , min0 , sec0 , yr1 , month1 , day1 , hr1 , min1 , sec1 , update_int = 60):
    """update_int (s)"""

    start_time = satkit.time(yr0 , month0 , day0 , hr0 , min0 , sec0)
    end_time = satkit.time(yr1 , month1 , day1 , hr1 , min1 , sec1)
    sec = sec0
    min = min0
    hr = hr0
    day = day0
    month = month0
    yr = yr0

    while start_time < end_time:
        julian_time , fr = jd.from_gregorian(yr0 , month0 , day0 , hr0 , min0 , sec) , 0.0
        e , r , v = sc.sgp4(julian_time , fr)
        rm = np.array(r) * 10**3
        vm = np.array(v) * 10**3
        t_utc = satkit.time(yr0 , month0 , day0 , hr0 , 33 , 0)
        q = satkit.frametransform.qteme2itrf(t_utc)
        itrf_pos = q * np.array(rm)
        itrf_vel = q * np.array(vm)
        az = np.arctan(itrf_pos[0] / itrf_pos[1]) * 180 / np.pi
        el = np.arctan(itrf_pos[1] / itrf_pos[2]) * 180 / np.pi
        time.sleep(update_int)
        sec += update_int
        k = round(sec / 60)
        hr += k

        print(k)
    
