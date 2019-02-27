#!/usr/bin/python3

'''
This script is used to calculate the transition probability of ATGC in a given genome.
Usage: transition_prob_acgt.py
Call the function transition_prob_acgt("<--Name of the file-->") and the transition probability of the nucleotides will be displayed on the terminal.
'''

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

transition_prob_acgt("Tcas_genome_5_2.fna")
transition_prob_acgt("Dmel_genome_6.fna")
transition_prob_acgt("Agam_genome_3.fna")
