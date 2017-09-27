# HW2 README

### Assignment 1
I wrote a script to stream real-time bus data from MTA through the MTA bys time interface.

file show_bus_location.py will take in API key information and the requested bus line information, then print a list of current running buses along with their information. Please follow the example below to use the script:

sample input:
```
python show_bus_locations.py xxxxx-xxxxx-xxxxx-xxxxx-xxxxx B52
```
sample output:
```
Bus Line : B52
Number of Active Buses : 5
Bus 0 is at latitude 40.687241 and longitude -73.941661
Bus 1 is at latitude 40.690822 and longitude -73.920759
Bus 2 is at latitude 40.688363 and longitude -73.979563
Bus 3 is at latitude 40.688282 and longitude -73.979356
Bus 4 is at latitude 40.686839 and longitude -73.964694
```
### Assignment 2
Similar to previous assignment, I wrote a script file get_bus_info.py which will take in the API key information and bus line number and a csv file name then generate a csv file that contains the location of buses, current stops of buses and next stops for buses.

sample input:
```
python get_bus_info.py xxxx-xxxx-xxxx-xxxx-xxxx <BUS_LINE> <BUS_LINE>.csv
```
sample output:
```
Latitude,Longitude,Stop Name,Stop Status
40.755489,-73.987347,7 AV/W 41 ST,at stop
40.775657,-73.982036,BROADWAY/W 69 ST,approaching
40.808332,-73.944979,MALCOLM X BL/W 127 ST,approaching
40.764998,-73.980416,N/A,N/A
40.804702,-73.947620,MALCOLM X BL/W 122 ST,< 1 stop away
40.776950,-73.981983,AMSTERDAM AV/W 72 ST,< 1 stop away
40.737650,-73.996626,AV OF THE AMERICAS/W 18 ST,< 1 stop away
```
Note: I am currently still in the process of implementing the N/A output feature of this script file.

### Assignment 3 and extra_credit
In this assignment, I randomly read a csv file from the CUSP data facility  into dataframe and dropped all but two numerical columns, then plot them into a scatter plot with one column as x and the other as y axis.
The extra_credit problem is similar, but I used the datetime function from pandas to convert the date/time column into a datetime column, then plot it with date/time as the x axis.
