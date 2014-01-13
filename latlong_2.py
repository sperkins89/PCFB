#! /usr/bin/env python
import re

def decimalat(DegString):
	#This function requires that the re module is already imported.
	#Takes a string with format "34 56.78 N" and returns decimal degrees
	SearchStr = '(\d+) ([\d\.]+) (\w)'
	Result = re.search(SearchStr, DegString)
	
	#Get captured character groups, as defined by parentheses in the regular expression,
	#convert numbers to floats, and assign to variables with meaningful names.
	Degrees = float(Result.group(1))
	Minutes = float(Result.group(2))
	Compass = Result.group(3).upper() 
	
	#Calculate the decimal degrees
	DecimalDegree = Degrees + Minutes/60
	
	#If compass direction is South or West, make sign of coordinate negative
	if Compass == 'S' or Compass == 'W':
		DecimalDegree = -DecimalDegree
		
	return DecimalDegree
		
#Set the input file name
InFileName = "Marrus_claudanielis.txt"

#Derive output file from input file name
OutFileName = 'dec_' + InFileName

#Give option to write or just print to screen
WriteOutFile = True

#Open the input file for reading
InFile = open(InFileName, 'r')

HeaderLine = 'dive\tdepth\tlatitude\tlongitude\tdate\tcomment'
print HeaderLine

#Open output file, if desired.  Do outside loop.
if WriteOutFile:
	#open the output file
	OutFile = open(OutFileName, 'w')
	OutFile.write(HeaderLine + '\n')

#Initialize line counter
LineNumber = 0


#Loop through each line of file
for Line in InFile:
	#skip the header line
	if LineNumber > 0:
		#Remove line-ending characters
		Line = Line.strip('\n')
		
		#Separate line into components
		ElementList = Line.split('\t')
		
		Dive = ElementList[0]
		Date = ElementList[1]
		Depth = ElementList[4]
		Comment = ElementList[5]
		
		LatDegrees = decimalat(ElementList[2])
		LonDegrees = decimalat(ElementList[3])
		print "Lat: %f, Lon: %f" % (LatDegrees, LonDegrees)
		
		#create string to 5 decimal places padded up to 10 total characters
		#using line continuation character \
		OutString = "%s\t%4s\t%10.5f\t%10.5f\t%9s\t%s" % \
							(Dive, Depth, LatDegrees, LonDegrees, Date, Comment)
		
		print OutString
		if WriteOutFile:
			OutFile.write(OutString+'\n')
		
	#Index the counter to keep track of line numbers
	LineNumber += 1

#After the loop is closed, close the files
InFile.close()
if WriteOutFile:
	OutFile.close()
