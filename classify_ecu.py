#	Authored: Max Pfeiffer - 2018
#	This software is free and open to anyone who wishes to use it
#!/usr/bin/python

# returns the ECU id in plain text based on the hex value passed 
def classify_ecu(ecu_id):
	if(ecu_id < 14):
		return "Powertrain - Integration / Manufacturer Expansion"
	elif(ecu_id < 23):
		return "Powertrain - Engine Controllers"	
	elif(ecu_id < 31):
		return "Powertrain - Transmission Controllers"
	elif(ecu_id < 39):
		return "Chassis - Integration / Manufacturer Expansion"
	elif(ecu_id < 47):
		return "Chassis - Brake Controllers"
	elif(ecu_id < 55):
		return "Chassis - Steering Controllers"
	elif(ecu_id < 63):
		return "Chassis - Suspension Controllers"
	elif(ecu_id < 87):
		return "Body - Integration / Manufacturer Expansion"
	elif(ecu_id < 95):
		return "Body - Restraints"
	elif(ecu_id < 111):
		return "Body - Driver Information / Displays"
	elif(ecu_id < 127):
		return "Body - Lighting"
	elif(ecu_id < 143):
		return "Body - Entertainment / Audio"
	elif(ecu_id < 151):
		return "Body - Personal Communication"
	elif(ecu_id < 159):
		return "Body - Climate Control (HVAC)"
	elif(ecu_id < 191):
		return "Body - Convenience (Doors, Seats, Windows, etc.)"
	elif(ecu_id < 197):
		return "Body - Security"
	elif(ecu_id == 200):
		return "EV - Utility Connection Services"
	elif(ecu_id == 201): 
		return "EV - AC/AC Converter"
	elif(ecu_id == 202): 
		return "EV - AC/DC Converter"
	elif(ecu_id == 203):
		return "EV - Energy Storage"