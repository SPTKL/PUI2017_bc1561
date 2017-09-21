__author__ = 'Baiyue Cao (ID:bc1561)'
import os
import sys
import pylab as pl
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

info_input = sys.argv
my_key = info_input[1]
bus_line = info_input[2]
PUIdata = os.getenv("PUIDATA")
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + my_key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

def print_info(bus_line, data):
    """given a bus line, print the bus name,
    number of vehicles and the current position"""
    bus_info = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    bus_count = len(bus_info)
    print(bus_line)
    print('Number of Active Buses : ' + str(len(bus_info)))
    for i in range(bus_count):
        location = bus_info[i]['MonitoredVehicleJourney']['VehicleLocation']
        lat = location['Latitude']
        lon = location['Longitude']
        position_info = 'Bus ' + str(i) + ' is at latitude ' + str(lat) + ' and longitude ' + str(lon)
        print(position_info)

print_info(bus_line, data)
