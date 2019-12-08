#!/usr/bin/env python
# coding: utf-8

# In[2]:


from matplotlib import *
import ephem
import time
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
tripoli=ephem.Observer() #Defining ground staion position
obs_latitude = 19.0760 #tripoli, Libya Latitude
obs_longitude = 72.8777 #tripoli, Libya Longitude
tripoli.lat = '19.0760'
tripoli.lon = '72.8777'

# TLE of ORBCOMM

orbcomm = ephem.readtle(
'Molniya 1-62',
'1 15214U 84089A   19048.31668002 -.00000855  00000-0 -69776-2 0  9997',
'2 15214  62.7641 196.3698 7128636 263.8284  18.2046  1.97944941220181')

# setting observation date any day btw 20th-24th of December, 2017

track_date = ephem.Date((2018,12,24))
orbcomm.compute(tripoli)
print(ephem.Date(track_date))
print("Orbcomm is at", orbcomm.az, orbcomm.alt)

# azimuth angle n altitude az — Azimuth east of north
#alt — Altitude above horizon

print("Orbcomm is at", orbcomm.sublong, orbcomm.sublat)

#Geographic point beneath satellite:sublat — Latitude (+N),
#sublong — Longitude (+E)

print ("Distance between observer and satellite",orbcomm.range)

longList=[];
latList=[];
visible_latList = [];
visible_longList = [];
elev_angle = [];
azimuth_angle=[];
dist_sat_obs=[];
doppler_shift=[];
time = [];
f = 8345 * 10^6; # Emitted frequency
c = 3 * 10^8; #velocity of light
for i in range(1,1440): #First exemplary pass
    tripoli.date=track_date
    track_date=tripoli.date + (ephem.minute);
    orbcomm.compute(tripoli);
    longList.append(orbcomm.sublong*180.0/np.pi)
    latList.append(orbcomm.sublat*180.0/np.pi)
    elev_angle.append(orbcomm.alt*180.0/np.pi)
    azimuth_angle.append(orbcomm.az*180.0/np.pi)
    dist_sat_obs.append(orbcomm.range)
    doppler_shift.append((orbcomm.az*f)/c)
    if orbcomm.alt*180.0/np.pi > 5 : #computing data during connection time
        visible_latList.append(orbcomm.sublat*180.0/np.pi)
        visible_longList.append(orbcomm.sublong*180.0/np.pi)
        time.append(i) #time axis

# plotting the satellite track, observer location and connection time on world map for 24 hours

plt.figure(figsize=(14,8))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()

# Location of Tripoli

plt.plot(72.8777,19.0760,color='blue', linewidth=2, marker='o',transform=ccrs.Geodetic(),)

# Location of satellite

plt.plot(orbcomm.sublong*180.0/np.pi,orbcomm.sublat*180.0/np.pi,color='blue', linewidth=4, marker='o',transform=ccrs.Geodetic(),)
ax.plot(longList,latList,"r*",ms=5,transform=ccrs.Geodetic())
ax.gridlines()
plt.show()

# plotting the satellite track when its visible to the observer

plt.figure(figsize=(14,8))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()

# Location of Tripoli
plt.plot(72.8777,19.0760,color='blue', linewidth=2, marker='o',transform=ccrs.Geodetic(),)
ax.plot(visible_longList,visible_latList,"r*",ms=5,transform=ccrs.Geodetic())
ax.gridlines()
plt.show()

## For one exemplary pass

longList_ep = [];
latList_ep = [];
elev_angle_ep = [];
azimuth_angle_ep = [];
dist_sat_obs_ep = [];
time_ep = []
for l in range(1,1440):
    if (l>794 and l<806):
        longList_ep.append(longList[l])
        latList_ep.append(latList[l])
        elev_angle_ep.append(elev_angle[l])
        azimuth_angle_ep.append(azimuth_angle[l])
        dist_sat_obs_ep.append(dist_sat_obs[l])
        time_ep.append(l)

# plotting the satellite track when its visible to the observer for one EP

plt.figure(figsize=(14,8))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()

# Location of Tripoli

plt.plot(72.8777,19.0760,color='blue', linewidth=2, marker='o',transform=ccrs.Geodetic(),)
ax.plot(longList_ep,latList_ep,"r*",ms=5,transform=ccrs.Geodetic())
ax.gridlines()
plt.show()

#plotting elevation and azimuth

plt.figure(figsize=(12,7))
plt.plot(time,elev_angle)
plt.xlabel('Time in minutes')
plt.ylabel('Elevation in $\circ$')
plt.title('Elevation v/s time')
plt.grid()
plt.show()
plt.figure(figsize=(12,7))
plt.plot(time,azimuth_angle,'g')
plt.xlabel('Time in minutes')
plt.ylabel('Azimuth in $\circ$')
plt.title('Azimuth v/s time')
plt.grid()
plt.show()

#plotting distance between satellite and ground station

plt.figure(figsize=(12,7))
plt.plot(time,dist_sat_obs)
plt.xlabel('Time in minutes')
plt.ylabel('Distance in meter ')
plt.title('Distance of the satellite from observer v/s time')
plt.grid()
plt.show()

#plotting doppler frequency shift

plt.figure(figsize=(12,7))
plt.plot(time,doppler_shift)
plt.xlabel('Time in minutes')
plt.ylabel('Doppler frequency in Hertz ')
plt.title('Doppler frequency v/s time')
plt.grid()
plt.show()

##Plot of Azimuth, Elevation & distance between satellite and the observer for one exemplary overpass

plt.figure(figsize=(12,7))
plt.plot(time_ep,azimuth_angle_ep,'g')
plt.xlabel('Time in minutes')
plt.ylabel('Azimuth in degree')
plt.title('Azimuth v/s time')
plt.grid()
plt.figure(figsize=(12,7))
plt.plot(time_ep,elev_angle_ep,'r')
plt.xlabel('Time in minutes')
plt.ylabel('Elevation in degree')
plt.title('Elevation v/s time')
plt.grid()
plt.figure(figsize=(12,7))
plt.plot(time_ep,dist_sat_obs_ep)
plt.xlabel('Time in minutes')
plt.ylabel('Distance in meter ')
plt.title('Distance of the satellite from observer v/s time')
plt.grid()
plt.show();


# In[ ]:





# In[ ]:




