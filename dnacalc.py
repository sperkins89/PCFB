#! /usr/bin/env python
DNASeq = 'ATGTCTCATTCAAAGCA'
#DNASeq = raw_input("Enter a DNA sequence: ")
DNASeq = DNASeq.upper()
DNASeq = DNASeq.replace(" ", "")
print 'Sequence:', DNASeq
SeqLength = float(len(DNASeq))
print 'Sequence Length:', SeqLength
NumberA = DNASeq.count('A')
NumberC = DNASeq.count('C')
NumberG = DNASeq.count('G')
NumberT = DNASeq.count('T')

#First way to print bases
#print 'A:', NumberA/SeqLength
#print 'C:', NumberC/SeqLength
#print 'G:', NumberG/SeqLength
#print 'T:', NumberT/SeqLength

#Using % operator practice.
#print "There are %d A bases." % (NumberA)

#Illustration of combining two uses of %
#print "A occurs in %d bases out of %d." % (NumberA, SeqLength)

#Practicing using operator to specify number of digits
#print "A occurs in %.2f of %d bases." % (NumberA/SeqLength, SeqLength)

print "A: %.1f%%" % (100 * NumberA / SeqLength)
print "C: %.1f%%" % (100 * NumberC / SeqLength)
print "G: %.1f%%" % (100 * NumberG / SeqLength)
print "T: %.1f%%" % (100 * NumberT / SeqLength)

TotalStrong = NumberC + NumberG
TotalWeak = NumberA + NumberT

if SeqLength >= 14:
	#formula for sequences greater than 14 nucleotides long
	MeltTempLong = 64.9 + 41 * (TotalStrong - 16.4) / SeqLength
	print "Tm Long (>14): %.1f C" % (MeltTempLong)
else:
	#formula for sequences less than 14 nucleotides long
	MeltTemp = (4 * TotalStrong) + (2 * TotalWeak)
	print "Melting Temp : %.1f C" % (MeltTemp)
