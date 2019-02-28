# 	Converts the data in a standard Cabana output log format to 
# 	a comma separated list of integers, base 10, that can be copied
#	into a C/C++ program. 
# 
#	Usage: python data_to_ints.py "source.csv"
#
#	Result:	"int_source.csv"

import sys 
import csv

source = open(sys.argv[1], "w+")
src_data = csv.reader(source, delimiter = ",", quotechar = "|")

dest_data = open("hex"+sys.argv[1], "w+")
data_writer = csv.writer(dest_data, delimiter = ",")
header = 1
for row in src_data:
	if header: 
		data_writer.writerow(row)
		header = 0
	else: 
		time = row.pop(0)
		addr = row.pop(0)
		bus = row.pop(0)
		data = row.pop(0)
		print data 

		# need to calculate the length of this data and save that parameter to the data_len
		# check odd-value case 
		if len(data) % 2 > 0:
			data.insert(0,"0")					
			data_len = len(data)/2

		#list for saving the output 
		output_buf = []		

		# need to concatenate every two bytes of the hex 	
		for i in range(0,data_len):
			# pop the two bytes off of the data, or two entries from the list and concatenate them, then add them back to the end of the list 
			b0 = msg_data.pop()	
			# handle the case where the the msg_data is empty.. 
			if len(msg_data) < 1: 
				b1 = "0"
			else:	
				b1 = msg_data.pop()
			concat = b1 + b0
			concat.upper()
			concat = "0x" + concat

			output_buf.insert(0,concat)

		entry = [time, addr, bus, output_buf]
		data_writer.writerow(entry)


dest_data.close()
src_data.close()