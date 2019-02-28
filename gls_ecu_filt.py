#	Authored: Max Pfeiffer - 2018
#
#	Filters ID information out of a gmlanls log, pass as many ids to filter as needed 
#
#	Usage: 	python gls_ecu_filt.py "gls_info_cabana_logfile.csv" "0xAA" "0xBB" ...
#		"gls_info_cabana_logfile.csv" = the file to decode 
#		"0xAA" = first id to filter 
#		"0xBB" = second id to filter 
# 		etc.. 
#
#	Output: ecu_filt_gls_info_cabana_logfile.csv 
#		removes the filtered ids from the input file 
#
#
#!/usr/bin/python
import sys 
import csv

#get the input arguments 
filename = sys.argv[1]
filt_ids = [] 

if len(sys.argv) < 3:
	sys.exit("please specify ECU ids to filter")

for i in range(0,(len(sys.argv)-2)):
	filt_ids.append(sys.argv[i+2])

control = open(filename) 
control_csv = csv.reader(control, delimiter = ",", quotechar = "|")
header = 1 

new_log = open("ecu_filt_" + filename, "w+")							
new_writter = csv.writer(new_log, delimiter = ",")
new_writter.writerow(["Time", "ID", "Bus", "Data", "Priority","Arbitration","ECU ID", "ECU FAMILY"]) 

for row in control_csv:
	if header:
		header = 0 
	else: 
		if(len(row) > 7):
			time = row.pop(0)
			can_id = row.pop(0)
			bus = row.pop(0)
			data = row.pop(0)
			prior = row.pop(0)
			arb = row.pop(0)
			ecu_id = row.pop(0)
			ecu_fam = row.pop(0)
		else: 
			time = row.pop(0)
			can_id = row.pop(0)
			bus = row.pop(0)
			data = row.pop(0)
			prior = row.pop(0)
			arb = row.pop(0)
			ecu_id = row.pop(0)
			ecu_fam = ""
		# check to see if we should save it 
		if(ecu_id in filt_ids):
			new_writter.writerow([time, can_id, bus, data, prior, arb, ecu_id, ecu_fam])	

new_log.close()





