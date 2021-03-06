#	Authored: Max Pfeiffer - 2018
#
#	Reads the .csv file format generated by Comma Ai's Cabana and converts to
#	the generic format supported for use with Collin Kidder's SavvyCAN 
#
#	Preconditions: 	sourcefilename.csv 
#					Bus ID of interest (i.e. "1") 
#	
#	Outputs:		savvy_sourcefilename.csv 
#					
#	Example: $ python savvy_convert.py cabana_output.csv 1 


#!/usr/bin/python
import sys 
import csv

header = 1

with open(sys.argv[1]) as original:
	og_data = csv.reader(original, delimiter = ",", quotechar = "|")
	# make a new file as the output file 
	savvy_data = open("savvy_"+sys.argv[1], "w+")							
	savvy_writer = csv.writer(savvy_data, delimiter = ",")
	savvy_writer.writerow(["ID", "Data Bytes"])  
	
	for row in og_data:
		if header:
			header = 0
		else: 
			if(row.pop(2) == sys.argv[2]):
				msg_data = list(row.pop(2))
				msg_bytes = "" 
				addr = str(hex(int(row.pop(1))))
				addr = list(addr)
				addr.remove("x")
				while len(addr) < 8:
					addr.insert(0,0) 
				str_addr = ""
				while len(addr) > 0:
					str_addr = str(addr.pop()) + str_addr
				addr = str_addr.upper()

				# generate and write the data bytes in hex, upper 
				if(len(msg_data)):	# making sure its not empty 
					if len(msg_data) == 1: 
						savvy_writer.writerow([addr, "0"+(msg_data.pop(0)).upper()]) 
					elif len(msg_data) < 2: 
						savvy_writer.writerow([addr,(msg_data.pop(0)+msg_data.pop[0]).upper()])
					else: 
						for i in range(0,len(msg_data)/2): 
							msg_bytes+=msg_data.pop(0)+msg_data.pop(0)+ " "
						savvy_writer.writerow([addr, msg_bytes.upper()])

savvy_data.close()
original.close()
