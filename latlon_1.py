#! /usr/bin/env python

#Set the input file name
InFileName = "Marrus_claudanielis.txt"

#Open the input file for reading
InFile = open(InFileName, 'r')

#Initialize line counter
LineNumber = 0

#Loop through each line of file
for Line in InFile:
	#Remove line-ending characters
	Line = Line.strip('\n')
	#Print the line
	print LineNumber, ': ', Line
	
	#Index the counter to keep track of line numbers
	LineNumber = LineNumber +1

#After the loop is closed, close the file
InFile.close()