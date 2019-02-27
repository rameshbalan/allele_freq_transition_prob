#!/usr/bin/python3

'''
This script is used to calculate the frequency of each nucleotide. This script doesn't count anything except ACGT.
Usage: python3 acgt_freq.py
Call the function count_ACGT("<--Name of the file-->") and the frequency of the nucleotides will be displayed on the terminal.
'''

#define a function to count ATGCs
def count_ACGT(genomefile):

#declaring variables for counting:
	count_A = 0
	count_C = 0
	count_G = 0
	count_T = 0
	count_ACGT = [0,0,0,0]

	with open(genomefile,"r") as infile:
#looping through each line
		for line in infile:

			if not line.startswith(">"):
#spliting the line into individual nucleotides
				split_line = list(line)
#counting the nucleotides in each line
				for nucleotide in split_line:

					if nucleotide == "A":

						count_A += 1

					elif nucleotide == "C":

						count_C += 1

					elif nucleotide == "G":

						count_G += 1

					elif nucleotide == "T":

						count_T += 1

	count_ACGT[0] = ((count_A)/(count_A+count_C+count_G+count_T))
	count_ACGT[1] = ((count_C)/(count_A+count_C+count_G+count_T))
	count_ACGT[2] = ((count_G)/(count_A+count_C+count_G+count_T))
	count_ACGT[3] = ((count_T)/(count_A+count_C+count_G+count_T))

	print("The name of the file is:",genomefile)
	print("The frequency of ACGT is as follows:\n")
	print("A:",count_ACGT[0])
	print("C:",count_ACGT[1])
	print("G:",count_ACGT[2])
	print("T:",count_ACGT[3])
#return acgt_counts
	return count_ACGT

count_ACGT("Tcas_genome_5_2.fna")
count_ACGT("Dmel_genome_6.fna")
count_ACGT("Agam_genome_3.fna")