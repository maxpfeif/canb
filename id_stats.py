#	Authored: Max Pfeiffer - 2018
#
#	Reads log files in Cabana's .csv format and produces a .csv file with the 
# 	messages belonging to each unique id. Also produces a file containing the averating message period 
#	
#	Call: 	python id_stats.py "idfilename.csv" 
#			control.csv is the reference log file (i.e. quiescent, no changes)
#			new.csv is the variant log file 
# 			bus is the target bus we wish to analyze from the Cabana log 
#	
#	Result: CSV file with a list of CAN messages, includign the ID, and their corresponding average period  
#
#	a series of files "idx_messages.csv" for each unique ID in the log
# 				a periodic timing file, periods.csv, contianing the periods for each 
#				unique message ID logged into its own output file 
#
#	Dependencies: 	Requires that the get_diffs.py, get_unique.py and filter_id.py files 
# 					are in the PWD 
#
#	This software is free and open to anyone who wishes to use it

#!/usr/bin/python