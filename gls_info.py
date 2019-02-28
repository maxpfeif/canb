#	Authored: Max Pfeiffer - 2018
#
#	Adds the extended ID information to a GMLANLS log. 
#
#	Usage: 	python gls_info.py "cabana_logfile.csv" 
#		"cabana_logfile.csv" = the file to decode 
#
#	Output: gls_info_cabana_logfile.csv 
#		with added columns containing Priority,Arbitration,ECU ID,ECU FAMILY
#
#
#!/usr/bin/python
import sys 
import csv
from decimal import *
from classify_ecu import * 

# open the target file 
filename = sys.argv[1]

# saves a .csv file with all of the additional id information
def add_id_information(filename):	
	control = open(filename) 
	control_csv = csv.reader(control, delimiter = ",", quotechar = "|")
	header = 1 

	new_log = open("gls_info_" + filename, "w+")							
	new_writter = csv.writer(new_log, delimiter = ",")
	new_writter.writerow(["Time", "ID", "Bus", "Data", "Priority","Arbitration","ECU ID", "ECU FAMILY"]) 

	for row in control_csv:
		if header:
			header = 0 
		else: 
			# process the information fromthe bus 
			time = row.pop(0)
			can_id = row.pop(0)
			bus = row.pop(0)
			data = row.pop(0)

			if(can_id > 4095): # extended ID, lets print some additional information 
				# find the priority 
				priority = int(can_id) >> 26

				# find the arb id
				arbitration = (int(can_id) >> 13) & 8191

				# find the ecu id 
				ecu_id = hex(int(can_id) & 8191)

				ecu_fam = classify_ecu(int(can_id) & 8191)

				new_writter.writerow([time, can_id, bus, data, priority, arbitration, ecu_id, ecu_fam])
			else: 
				new_writter.writerow([time, can_id, bus, data])
	new_log.close()

add_id_information(filename)