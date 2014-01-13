#! /usr/bin/env python

#Set the input file name
InFileName = "Marrus_claudanielis.txt"

#Open the input file for reading
InFile = open(InFileName, 'r')

#Initialize line counter
LineNumber = 0

#Open output file for writing
OutFileName = InFileName + '.kml'

OutFile = open(OutFileName, 'w')

#Loop through each line of file
for Line in InFile:
	#skip the header line
	if LineNumber > 0:
		#Remove line-ending characters
		Line = Line.strip('\n')
		#Separate line into components
		ElementList = Line.split('\t')
		
		#Use % operator to generate a string
		OutputString = "Depth: %s\t Lat: %s\t Lon:%s" % \
			(ElementList[4], ElementList[2], ElementList[3])
		print OutputString
		
		OutFile.write(OutputString+'\n')
		
	#Index the counter to keep track of line numbers
	LineNumber = LineNumber +1

#After the loop is closed, close the file
InFile.close()
OutFile.close()
