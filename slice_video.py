#https://github.com/SeedlingsBabylab/subregsplice/blob/master/subrsplice.py#L56
import csv
import os

csvInputFile = 'speech_17275_verbonset_cleaned.csv'
csvHolder = []
with open(csvInputFile, newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader:
		csvHolder.append(row)
csvFinal = [[0 for x in range(4)] for y in range(len(csvHolder))]

counter = 1
for row in range(0,len(csvHolder)): 
	csvFinal[row][0] = str(csvHolder[row][0]) + '.mov' #set file input name
	csvFinal[row][2] = str(float(csvHolder[row][1])-3)#set onset time
	csvFinal[row][3] = str(5) #set offset time
	template = "{}_{}_{}_{}.mov"
	prefix = str(csvFinal[row][0]).replace('.mov','')
	kidID = prefix[-5:]
	#onset = "{:0.2f}".format(float(csvFinal[row][2]))
	#onset_Dash = onset.replace(".","-")
	verb = csvHolder[row][2]
	#csvFinal[row][1] = template.format(verb,kidID,counter,onset_Dash) #set file output name
	csvFinal[row][1] = template.format(verb,kidID,counter,"5sec") #set file output name
	counter= counter+1


for row in range(0,len(csvFinal)):
	onsetTime = csvFinal[row][2] #grabs onset time
	timeDiff = csvFinal[row][3] #grabs time difference
	fileName = csvFinal[row][0] #sets input filename
	outputPath = csvFinal[row][1] #sets output path
	command = ["ffmpeg","-ss",str(onsetTime),"-t",str(timeDiff),"-i",str(fileName),str(outputPath),"-y"]
	#command = ["ffmpeg","-ss",str(onsetTime),"-t",str(timeDiff),"-i",str(fileName),"-an",str(outputPath),"-y"]
	command_string = " ".join(command)
	print(command_string)
	os.system(command_string)
	'''
	beepString = str(outputPath).replace(".mov","_beep.mov")
	command2 = ["ffmpeg","-i", str(outputPath), "-itsoffset","3","-i","beep2.mp3", "-map","0:0","-map","1:0","-preset","ultrafast",beepString]
	command_string2 = " ".join(command2)
	os.system(command_string2)'''