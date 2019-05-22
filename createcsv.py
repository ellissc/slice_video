import csv
with open('testValues.csv','w',newline='') as csvfile:
	writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	writer.writerow(['__20160212_17275']+[50.3] + ["spin"])
	writer.writerow(['__20160212_17275']+[80.5555]+["rollover"])
	writer.writerow(['__20160212_17275']+[142.999393]+["sit"])
	writer.writerow(['__20160212_17275']+[172]+["yell"])
	