#!/usr/bin/python3

'''
Usage: python3 allele_freq_and_transition_prob.py
This script is used to 
	1. Calculate the frequency of each nucleotide. This script doesn't count anything except ACGT.
		a) Call the function count_ACGT("<--Name of the file-->") and the frequency of the nucleotides will be displayed on the terminal.
	2. This script is used to calculate the transition probability of ATGC in a given genome.
		b) Call the function transition_prob_acgt("<--Name of the file-->") and the transition probability of the nucleotides will be displayed on the terminal.
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

#define the function
def transition_prob_acgt(genomefile):

	#declaring variables for counting:
	prob_A_to_N = [0,0,0,0]
	prob_C_to_N = [0,0,0,0]
	prob_G_to_N = [0,0,0,0]
	prob_T_to_N = [0,0,0,0]
	prob_ACGT = [prob_A_to_N,prob_C_to_N,prob_G_to_N,prob_T_to_N]
	total_A_to_N = 0
	total_C_to_N = 0
	total_G_to_N = 0
	total_T_to_N = 0

	with open(genomefile,"r") as infile:
#looping through each line
		for line in infile:

			if not line.startswith(">"):
#spliting the line into individual nucleotides
				split_line = list(line)
#counting the nucleotides in each line with respect to the previous nucleotide
				for i in range(0,len(split_line)):

					try:

						if previous_nucleotide == "A":

							if split_line[i] == "A":

								prob_A_to_N[0] += 1

								previous_nucleotide = split_line[i]

							elif split_line[i] == "C":

								prob_A_to_N[1] += 1

								previous_nucleotide = split_line[i]

							elif split_line[i] == "G":

								prob_A_to_N[2] += 1

								previous_nucleotide = split_line[i]

							elif split_line[i] == "T":

								prob_A_to_N[3] += 1

								previous_nucleotide = split_line[i]

						elif previous_nucleotide == "C":

							if split_line[i] == "A":

								prob_C_to_N[0] += 1

								previous_nucleotide = split_line[i]

							elif split_line[i] == "C":

								prob_C_to_N[1] += 1

								previous_nucleotide = split_line[i]

							elif split_line[i] == "G":

								prob_C_to_N[2] += 1

								previous_nucleotide = split_line[i]

							elif split_line[i] == "T":

								prob_C_to_N[3] += 1

								previous_nucleotide = split_line[i]

						elif previous_nucleotide == "G":

							if split_line[i] == "A":

								prob_G_to_N[0] += 1

								previous_nucleotide = split_line[i]

							elif split_line[i] == "C":

								prob_G_to_N[1] += 1

								previous_nucleotide = split_line[i]

							elif split_line[i] == "G":

								prob_G_to_N[2] += 1

								previous_nucleotide = split_line[i]

							elif split_line[i] == "T":

								prob_G_to_N[3] += 1

								previous_nucleotide = split_line[i]

						elif previous_nucleotide == "T":

							if split_line[i] == "A":

								prob_T_to_N[0] += 1

								previous_nucleotide = split_line[i]

							elif split_line[i] == "C":

								prob_T_to_N[1] += 1

								previous_nucleotide = split_line[i]

							elif split_line[i] == "G":

								prob_T_to_N[2] += 1

								previous_nucleotide = split_line[i]

							elif split_line[i] == "T":

								prob_T_to_N[3] += 1

								previous_nucleotide = split_line[i]

					except UnboundLocalError:

						previous_nucleotide = split_line[i]

	total_A_to_N = prob_A_to_N[0]+prob_A_to_N[1]+prob_A_to_N[2]+prob_A_to_N[3]
	total_C_to_N = prob_C_to_N[0]+prob_C_to_N[1]+prob_C_to_N[2]+prob_C_to_N[3]
	total_G_to_N = prob_G_to_N[0]+prob_G_to_N[1]+prob_G_to_N[2]+prob_G_to_N[3]
	total_T_to_N = prob_T_to_N[0]+prob_T_to_N[1]+prob_T_to_N[2]+prob_T_to_N[3]
	prob_A_to_N[:] = [x / total_A_to_N for x in prob_A_to_N]
	prob_C_to_N[:] = [x / total_C_to_N for x in prob_C_to_N]
	prob_G_to_N[:] = [x / total_G_to_N for x in prob_G_to_N]
	prob_T_to_N[:] = [x / total_T_to_N for x in prob_T_to_N]
	prob_ACGT = [prob_A_to_N,prob_C_to_N,prob_G_to_N,prob_T_to_N]

	print("The name of the file is:",genomefile)
	print("Transition Probability of A, C, G, T")

#return transition probability
	print(prob_ACGT)
	return prob_ACGT

count_ACGT("Tcas_genome_5_2.fna")
count_ACGT("Dmel_genome_6.fna")
count_ACGT("Agam_genome_3.fna")

transition_prob_acgt("Tcas_genome_5_2.fna")
transition_prob_acgt("Dmel_genome_6.fna")
transition_prob_acgt("Agam_genome_3.fna")
