def plot(desc, value, scale):
	slength = int(desc.__len__()) 
	whitespace = (30 - (slength + 1)) *" "
	initial = str(desc) + ":" + whitespace + "-" + str(scale)
	if value != 0: 
		svalue = value

	if value < 0:
		line1 = initial + " [" + ((20 - (-1)*svalue)*" ") + "(|" + (((svalue*(-1)) - 2) * "=") + "8" + (" "*20) + "]" + " +" +str(scale);
		line2 = (55*" ") + str(svalue) + ((20 - svalue)*" ");
	if value == 0:
		line1 = initial + " [" + (" "*20) + "8" + (" "*20) + "]" + " +"+ str(scale);
		line2 = (55*" ") + "0";
	if value > 0:
		line1 = initial + " [" + (" "*20) + "8" + ((svalue - 2) * "=") + "D" + ((20 - svalue + 1)*" ") + "]" + " +" + str(scale);
		line2 = (55*" ") + str(svalue) + ((20 - svalue)*" ");

	print ('\n'+ line1)
	print (line2)

# plot("Shitting", 9, 10)
# plot("Shitting", 0, 50)
# plot("Shitting", -10, 50)
